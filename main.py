from utils import load_checkins, load_payments, load_members, generate_summary
from gpt_query import ask_gpt

def main():
    print("Loading data...")

    checkins_df = load_checkins()
    # print("Check-ins loaded:\n", checkins_df)

    payments_df = load_payments()
    # print("Payments loaded:\n", payments_df)

    members_df = load_members()
    # print("Members loaded:\n", members_df)

    print("Generating summary...")
    summary = generate_summary(checkins_df, payments_df, members_df)
    # print("SUMMARY:\n", summary)
    # included print statements for debugging and optional verification

    while True:
        question = input("\nAsk a question (or type 'exit'): ")
        if question.lower() == 'exit':
            break

        response = ask_gpt(summary, question)
        print("\n💡 GPT Response:")
        print(response)

if __name__ == "__main__":
    main()
