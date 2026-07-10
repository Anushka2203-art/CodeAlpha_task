print("Chatbot: Hi! I am a simple bot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower().strip()

    if "hello" in user_input or "hi" in user_input:
        print("Chatbot: Hello! How can I help you today?")
        
    elif "name" in user_input:
        print("Chatbot: My name is SimpleBot, your friendly intern assistant.")
        
    elif "how are you" in user_input or "how's it going" in user_input:
        print("Chatbot: I am doing great, thank you for asking! How are you?")
        
    elif "who made you" in user_input or "created you" in user_input:
        print("Chatbot: I was created by a student using Python!")
        
    elif "weather" in user_input:
        print("Chatbot: I don't have a thermometer, but I hope it's sunny where you are!")
        
    elif "time" in user_input or "date" in user_input:
        print("Chatbot: I don't have a live clock module yet, but you can check your device's screen!")
        
    elif "joke" in user_input:
        print("Chatbot: Why do programmers wear glasses? Because they can't C#! ")
        
    elif "what can you do" in user_input or "help" in user_input:
        print("Chatbot: I can chat with you, tell a joke, or answer basic questions. Try asking 'who made you'!")
        
    elif "bye" in user_input or "exit" in user_input:
        print("Chatbot: Goodbye! Good luck!")
        break  
        
    else:
        print("Chatbot: I'm still learning. I didn't quite understand that, but you can ask me something else!")