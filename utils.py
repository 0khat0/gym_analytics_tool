import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

def get_openai_key():
    return os.getenv("OPENAI_API_KEY")

def load_checkins(filepath="data/checkins.csv"):
    return pd.read_csv(filepath, parse_dates=["Date"])

def load_payments(filepath="data/payments.csv"):
    return pd.read_csv(filepath, parse_dates=["Payment Due Date", "Latest Payment"])

def load_members(filepath="data/members.csv"):
    return pd.read_csv(filepath, parse_dates=["Joined"])

def generate_summary(checkins_df, payments_df, members_df):
    summary = []
    today = pd.Timestamp(datetime.today().date())

    for _, member in members_df.iterrows():
        member_id = member["Member ID"]
        name = member["Name"]
        age = member["Age"]
        sex = member["Sex"]
        location = member["Location"]
        joined = member["Joined"].date()
        notes = member.get("Notes", "")
        months_active = (today.year - joined.year) * 12 + (today.month - joined.month)

        payment_row = payments_df[payments_df["Member ID"] == member_id]
        if payment_row.empty:
            due_date = "Unknown"
            last_payment = "Unknown"
            status = "Unknown"
        else:
            due_date_raw = payment_row.iloc[0]["Payment Due Date"]
            last_payment_raw = payment_row.iloc[0]["Latest Payment"]
            due_date = due_date_raw.date()
            last_payment = last_payment_raw.date()
            status = "Overdue" if today > due_date_raw else "Active"

        checkins = checkins_df[checkins_df["Member ID"] == member_id]
        checkin_dates_raw = checkins["Date"].dt.date.tolist()
        checkin_dates = [d.strftime("%B %d") for d in checkin_dates_raw]
        last_checkin = max(checkin_dates_raw).strftime("%B %d") if checkin_dates_raw else "No check-ins"

        member_json = {
            "Member ID": member_id,
            "Name": name,
            "Age": age,
            "Sex": sex,
            "Location": location,
            "Joined": str(joined),
            "Months Active": months_active,
            "Payment Due Date": str(due_date),
            "Last Payment Date": str(last_payment),
            "Status": status,
            "Check-ins": len(checkin_dates),
            "Check-in Dates": checkin_dates,
            "Last Check-in": last_checkin,
            "Notes": notes
        }

        summary.append(member_json)

    import json
    return json.dumps(summary, indent=2)

def generate_stats_summary(members_df, payments_df, checkins_df):
    summary = {}

    summary["Total Members"] = len(members_df)
    summary["Males"] = int((members_df["Sex"] == "M").sum())
    summary["Females"] = int((members_df["Sex"] == "F").sum())

    location_counts = members_df["Location"].value_counts().to_dict()
    summary["Members by Location"] = location_counts

    today = pd.Timestamp(datetime.today().date())
    payments_df["Overdue"] = payments_df["Payment Due Date"] < today
    summary["Overdue Members"] = int(payments_df["Overdue"].sum())
    summary["Active Members"] = int(len(payments_df) - summary["Overdue Members"])

    last_checkins = checkins_df.groupby("Member ID")["Date"].max()
    inactive_ids = last_checkins[last_checkins < (today - pd.Timedelta(days=10))].index.tolist()
    inactive_names = members_df[members_df["Member ID"].isin(inactive_ids)]["Name"].tolist()
    summary["Inactive (10+ days)"] = inactive_names

    return summary

def load_dataframes(checkins_file, payments_file, members_file):
    checkins = pd.read_csv(checkins_file)
    payments = pd.read_csv(payments_file)
    members  = pd.read_csv(members_file)
    return checkins, payments, members    