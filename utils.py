import pandas as pd
import os

def load_checkins(filepath="checkins.csv"):
    df = pd.read_csv(filepath, parse_dates=["Date"])
    return df

def load_payments(filepath="payments.csv"):
    df = pd.read_csv(filepath, parse_dates=["Payment Due Date", "Latest Payment"])
    return df

from datetime import datetime

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
        months_active = (today.year - joined.year) * 12 + (today.month - joined.month)

        # Payment Info
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

        # Check-ins
        checkins = checkins_df[checkins_df["Member ID"] == member_id]
        checkin_dates_raw = checkins["Date"].dt.date.tolist()
        checkin_dates = [d.strftime("%B %d") for d in checkin_dates_raw]
        last_checkin = max(checkin_dates_raw).strftime("%B %d") if checkin_dates_raw else "No check-ins"

        # Assemble member JSON block
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
            "Last Check-in": last_checkin
        }

        summary.append(member_json)

    # Return as a string (JSON-style)
    import json
    return json.dumps(summary, indent=2)



from dotenv import load_dotenv
load_dotenv()

def get_openai_key():
    return os.getenv("OPENAI_API_KEY")

def load_members(filepath="members.csv"):
    df = pd.read_csv(filepath, parse_dates=["Joined"])
    return df
