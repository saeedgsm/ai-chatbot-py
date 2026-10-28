import dotenv
import os
from openai import OpenAI

dotenv.load_dotenv()

llm = OpenAI(
    api_key=os.getenv('GROQ_API_KEY'),
    base_url="https://api.groq.com/openai/v1"
)

messages = [
    {'role': 'system', 'content': '''you are a helpful assistant.
    Your name is neon_bot. in the first response, introduce yourself.give short and concise answer'''}
]

total_tokens = 0

def bot(message):

    global total_tokens

    messages.append({"role": "user", "content": message})

    respone = llm.chat.completions.create(
        model='openai/gpt-oss-120b',
        messages=messages,
        temperature=0.7,
        max_tokens=100,
    )

    response_message = respone.choices[0].message.content
    messages.append({"role": "assistant", "content": response_message})

    total_tokens += respone.usage.total_tokens

    return response_message


def chat():
    print("Welcome to the Chat Bot! Type 'q' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == 'q':
            print("Goodbye!")
            break
        response = bot(user_input)
        print(f"Bot: {response}")


def main():
    chat()
    print(f'Consumed total tokens: {total_tokens}')


if __name__ == '__main__':
    main()
