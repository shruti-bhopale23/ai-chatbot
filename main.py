def chatbot():
    print("Bot:Hello! Type 'bye' to exit")
    while True:
        user_input = input ("You: ").lower()

        if user_input in ["hello","hi","hey"]:
            print("Bot: Hi there!")

        elif "how are you" in user_input:
            print("BOt: i am doing great!")    
        elif "name" in user_input:
            print("Bot:I am your Python chatbot")
        elif user_input == "bye":
            print("bot: Goodbye!")
            break
        else:
            print("Bot: I am confused")


chatbot()
