import pyjokes

def chat_bot():
    print("\nHello, User! I'm JokeBot")
    print("Type 'joke' to receive a joke, or 'exit' to end chat with JokeBot")

    while True:
        user_input = input("\nYou: ").lower()

        if user_input == "joke":
            bot_response = pyjokes.get_joke()
            print(f"JokeBot: {bot_response}")
        elif user_input == "exit":
            print("JokeBot: Mood lifted? Come back anytime!")
            break
        else:
            print("JokeBot: Sorry, I only respond to 'joke' or 'exit'")