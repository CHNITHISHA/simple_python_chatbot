import openai
import os


openai.api_key = os.getenv("KEY_Login_to_your_openai_from_there_take_api_key")  

def chat_with_gpt(chat_log):
    """Function to communicate with OpenAI's GPT model."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=chat_log
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    chat_log = []  # Stores conversation history
    n_remembered_post = 2  # Number of past messages to remember

    while True:
        user_input = input("You: ").strip()  # Get user input and remove extra spaces

        if user_input.lower() in ['quit', "exit", "bye"]:
            print("Chatbot: Goodbye! ")
            break  

        chat_log.append({'role': 'user', 'content': user_input})

        # Keep only the last `n_remembered_post` messages
        if len(chat_log) > n_remembered_post:
            chat_log = chat_log[-n_remembered_post:]

        response = chat_with_gpt(chat_log)  # Get response from GPT
        print("Chatbot:", response)

        chat_log.append({'role': "assistant", 'content': response})  # Store assistant's response
