import time

from src.agent.builder import build_agent


def main():

    agent = build_agent()

    print("=" * 50)
    print("AI Agent Started")
    print("Type 'exit' to quit.")
    print("=" * 50)

    while True:

        user_query = input("\nYou : ").strip()

        if user_query.lower() in {
            "exit",
            "quit",
            "bye",
        }:

            print("\n" + "=" * 50)
            print("Thank you for using AI Agent From Scratch.")
            print("Goodbye! 👋")
            print("=" * 50)

            break

        response = agent.run(user_query)

        print("\nAssistant:")
        print(response)


if __name__ == "__main__":
    main()