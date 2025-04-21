# gym_analytics_tool
Scalable, LLM-powered gym analytics tool that uses structured data and the OpenAI API to answer natural language questions about member activity, payments, and engagement. Modular, extensible, and API-ready.

# 🧠 AI-Powered Gym Analytics Tool (WIP)

This is a modular, AI-integrated analytics tool built for gyms and fitness spaces to streamline operational insights using large language models. The system takes structured data inputs (check-ins, payments, and member metadata) and enables managers to ask natural questions like:

> "Who hasn't shown up this week?"  
> "How many members are overdue?"  
> "Which members from Toronto checked in last month?"

Built in Python and powered by OpenAI's API, this project serves as a foundation for automating and scaling gym management workflows — from attendance tracking to payment reconciliation — without manually digging through spreadsheets.

---

## 💡 Features

- ✅ GPT-powered natural language Q&A engine
- ✅ Parses multiple structured data files (`checkins.csv`, `payments.csv`, `members.csv`)
- ✅ Dynamically computes payment status, active/inactive members, and time-based analytics
- ✅ JSON-style prompt summaries for accurate LLM reasoning
- ✅ Built to extend into APIs, UIs, or third-party integrations
- ✅ Can support check-ins via RFID, QR, mobile app, or API — implementation-agnostic

---

## 🚀 Why It Matters

This project demonstrates how LLMs can automate decision-making and operations for real businesses. It replaces manual filtering, Excel lookups, and if-statements with a single natural language interface.

> Designed to be scalable, API-driven, and framework-agnostic — adaptable to various check-in or CRM systems.

---

## 📦 Current Data Inputs

- `checkins.csv`: Timestamped check-in logs
- `payments.csv`: Payment due dates and most recent payments
- `members.csv`: Member profiles (age, gender, location, join date)

---

## 🔍 Example Queries

- "Who’s overdue on payments?"
- "List all female members from Toronto"
- "Who checked in more than 3 times this month?"
- "Which members joined this year and are still active?"
- "How many people came last Monday?"

---

## 🧱 Stack

- Python 3.x
- `pandas` for lightweight data manipulation
- OpenAI (`gpt-3.5-turbo`) for natural language processing
- `.env`-based config for API security

---

