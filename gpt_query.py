from openai import OpenAI
from utils import get_openai_key

client = OpenAI(api_key=get_openai_key())

def ask_gpt(summary_text, user_question):
    prompt = (
        "You are an assistant helping manage a gym. "
        "Here is the current members status:\n\n"
        f"{summary_text}\n\n"
        f"Now answer this question:\n{user_question}"
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # or "gpt-4"
        messages=[
            {"role": "system", "content": "You are a helpful assistant for gym analytics."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content
