# 🏋️ Gym Analytics Tool — GPT-Powered Insights for Fitness Spaces

A streamlined, AI-powered tool that helps gym managers gain insights into member activity, check-ins, and payments — all through natural language. Built using Python, Streamlit, and OpenAI’s GPT API.

> **🌐 Live Demo:** [gymanalyticstool-0khat0.streamlit.app](https://gymanalyticstool-0khat0.streamlit.app)

---

## 💡 Key Features

- **📊 Data-Driven Dashboard:** Upload `members.csv`, `checkins.csv`, and `payments.csv` to get instant gym-wide analytics.
- **💬 Natural Language Queries:** Ask questions like:
  - “Who hasn’t shown up in 10+ days?”
  - “Who are my most active members?”
  - “Which members are overdue on payment?”
- **🧠 GPT Integration:** Uses OpenAI's GPT-3.5 model to understand gym data and answer manager-level questions.
- **📈 Stats Summary:** Gender breakdown, overdue payments, member activity, and more.

---

## 🗂️ File Structure

```plaintext
gym_analytics_tool/
│
├── app.py               # Main Streamlit UI and app logic
├── gpt_query.py         # GPT logic (OpenAI chat API)
├── utils.py             # CSV loaders and summarizers
├── requirements.txt     # Python dependencies
├── .env                 # (local use) OpenAI API key
│
├── data/                # Your data folder
│   ├── members.csv
│   ├── checkins.csv
│   └── payments.csv
│
└── README.md
