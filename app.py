import streamlit as st
import pandas as pd
from utils import (
    load_dataframes,
    generate_summary,
    generate_stats_summary
)
from gpt_query import ask_gpt

st.set_page_config(page_title="Gym Analytics Tool", layout="wide")
st.title("💪 GPT-Powered Gym Analytics Tool")

st.markdown("Upload your gym's check-in, payment, and member data below.")

# Upload files
uploaded_checkins = st.file_uploader("📥 Upload checkins.csv", type="csv")
uploaded_payments = st.file_uploader("📥 Upload payments.csv", type="csv")
uploaded_members  = st.file_uploader("📥 Upload members.csv", type="csv")

if uploaded_checkins and uploaded_payments and uploaded_members:
    # Load CSVs into DataFrames
    checkins = pd.read_csv(uploaded_checkins, parse_dates=["Date"])
    payments = pd.read_csv(uploaded_payments, parse_dates=["Payment Due Date", "Latest Payment"])
    members = pd.read_csv(uploaded_members, parse_dates=["Joined"])


    st.success("✅ Data loaded successfully!")

    # Show preview
    with st.expander("📊 Preview Uploaded Data"):
        st.subheader("Members")
        st.dataframe(members)
        st.subheader("Payments")
        st.dataframe(payments)
        st.subheader("Check-ins")
        st.dataframe(checkins)

    # Generate summaries for GPT
    member_summary = generate_summary(checkins, payments, members)
    stats_summary = generate_stats_summary(members, payments, checkins)

    # Input for GPT question
    st.subheader("💬 Ask a question about your gym:")
    user_question = st.text_input("E.g. 'Who hasn't shown up recently?' or 'Which members are overdue?'")

    if st.button("Ask GPT") and user_question.strip():
        with st.spinner("Asking GPT..."):
            response = ask_gpt(member_summary, stats_summary, user_question)
        st.markdown("### 🧠 GPT Response")
        st.markdown(response)
else:
    st.info("Please upload all 3 files to begin.")
