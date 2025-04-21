import openai
import os
import json
from openai import OpenAI
from utils import get_openai_key

client = OpenAI(api_key=get_openai_key())

def ask_gpt(member_summary, stats_summary, user_question):
    system_message = {
        "role": "system",
        "content": (
            "You are a helpful assistant for a gym analytics tool. "
            "Use the provided stats summary for any counting, totals, or comparisons. "
            "Use the member data for behavioral patterns, notes, check-ins, and membership context. "
            "Avoid making up data. Be concise and helpful."
        )
    }

    prompt = (
        f"📊 Stats Summary:\n{json.dumps(stats_summary, indent=2)}\n\n"
        f"📋 Member Records:\n{member_summary}\n\n"
        f"Question: {user_question}"
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            system_message,
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content.strip()
