# 🧠 AI-Powered Gym Analytics Tool

A scalable, GPT-powered analytics assistant for gyms, dojos, and fitness centers.  
It reads structured data like member check-ins, payments, and personal details — and lets you ask real business questions in plain English.

> No more spreadsheets, no SQL, no filters. Just ask.

---

## ✅ Why We Built This

Gyms often track data in spreadsheets or internal systems, but owners and managers rarely have time to analyze trends or member behavior.

This project shows how **LLMs (Large Language Models)** like ChatGPT can automate those insights — from financial tracking to identifying at-risk members.

### 🔍 Built for:
- Managers who want **trend-level insights** (“Are female members showing up less this month?”)
- Admins tracking **payments and overdue follow-ups**
- Owners seeking **member retention and engagement analytics**
- Operators who want to **ask instead of code**

---

## 🧠 What It Does

- ✅ Loads data from CSVs (`checkins.csv`, `members.csv`, `payments.csv`)
- ✅ Dynamically builds structured summaries (status, check-in history, overdue status, personal notes)
- ✅ Passes clean JSON-like data to GPT for accurate soft analysis
- ✅ Lets you ask natural questions like:
  - "Who hasn’t shown up in 10+ days?"
  - "Any new members dropping off early?"
  - "Which members owe money but still attend?"
  - "List women under 30 who haven’t checked in this week"
  - "Give me trends or risks I should look at this month"

---

## 💡 Highlights

- ⚙️ Built in Python with `pandas` + OpenAI’s `gpt-3.5-turbo`
- 🔐 `.env` file support for secure API key management
- 🔄 Ready for Streamlit/web UI or API integration
- 🔓 Not locked to one system — works with QR, RFID, apps, or manual check-ins

---

## 📁 Current Data Inputs

- **`members.csv`**  
  Age, gender, location, join date, and personal notes

- **`checkins.csv`**  
  Timestamped gym check-ins with member ID

- **`payments.csv`**  
  Last payment and due date per member

---

## 💬 Example Queries (Manager-Friendly)

These show off GPT's soft skills — identifying trends, patterns, and priorities:

| Category | Sample Questions |
|----------|------------------|
| **Overdue** | “Who owes money but checked in this week?” |
| **Retention Risk** | “Who joined in the last 3 months but stopped coming?” |
| **Engagement** | “Which members checked in most this month?” |
| **Demographic Insights** | “How many women under 30 from Mississauga came last week?” |
| **Follow-Ups** | “Anyone with notes about coaching or disengagement?” |
| **Actionable Trends** | “Is engagement going down among Toronto members?” |

---

## 🛠️ How to Run Locally

```bash
git clone https://github.com/0khat0/gym_analytics_tool.git
cd gym_analytics_tool

# Install requirements (pip install pandas, openai, python-dotenv)
pip install -r requirements.txt

# Add your OpenAI key
echo OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxx > .env

# Run it
python main.py
