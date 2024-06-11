import re

# Define the patterns and responses
patterns = {
    "hi|hello": "Hello! How can I assist you today?",
    "how are you": "I'm a chatbot, so I'm always good! How can I assist you?",
    "what is your name": "I'm a chatbot created by Parth. You can call me ParthGPT.",
    "bye": "Goodbye! Have a great day!",
    "gyi": "Gyi! What can I do for you?",
    "story": "Once upon a time, in a land far, far away, there was a chatbot named ParthGPT. ParthGPT loved to help people with their questions and provide interesting information. One day, ParthGPT met a curious user who wanted to learn more about the world. Together, they explored many fascinating topics, from the depths of the oceans to the far reaches of space. And they both lived happily ever after, always learning and discovering new things. The end.",
     "poem": ("Roses are red, violets are blue,\n"
             "I'm PartGPT, here to chat with you.\n"
             "Ask me a question, or tell me a story,\n"
             "I'm here to help, in all of my glory.\n"
             "Let's have a chat, let's have some fun,\n"
             "Together we'll learn, until the day is done.")
}

# Function to match user input to patterns and return responses
def match_pattern(user_input):
    for pattern, response in patterns.items():
        if re.search(pattern, user_input):
            return response
    return "I'm sorry, I don't understand that. Can you please rephrase?"

# Chat loop
def chatbot():
    print("Chatbot: Hello! I am ParthGPT. How can I assist you today?")
    while True:
        user_input = input("You: ").lower()
        response = match_pattern(user_input)
        print(f"Chatbot: {response}")
        if "bye" in user_input:
            break

# Start the chatbot
if __name__ == "__main__":
    chatbot()