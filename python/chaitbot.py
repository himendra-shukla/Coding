def chatbot():
    print("Hello! I'm a simple chatbot. How can I help you today?")
    
    while True:
        user_input = input("You: ").lower()
        
        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How are you doing today?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, so I don't have feelings, but thank you for asking!")
        elif "what's your name" in user_input or "who are you" in user_input:
            print("Chatbot: I'm a simple chatbot created to assist you.")
        elif "bye" in user_input or "exit" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: I'm sorry, I don't understand that. Can you please rephrase?")

# Run the chatbot
chatbot()
