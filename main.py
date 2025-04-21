from utils import (
    load_checkins,
    load_payments,
    load_members,
    generate_summary,
    generate_stats_summary
)
from gpt_query import ask_gpt

def main():
    print("Loading data...")

    checkins_df = load_checkins()
    payments_df = load_payments()
    members_df = load_members()

    print("Generating summary...")
    member_summary = generate_summary(checkins_df, payments_df, members_df)
    stats_summary = generate_stats_summary(members_df, payments_df, checkins_df)

    print("\U0001F4CA Gym Stats Summary:")
    print(stats_summary)

    print("\n=== Ready for Q&A ===")

    while True:
        question = input("\nAsk a question (or type 'exit'): ")
        if question.lower() == 'exit':
            break

        response = ask_gpt(member_summary, stats_summary, question)
        print("\n\U0001F4A1 GPT Response:")
        print(response)

if __name__ == "__main__":
    main()
