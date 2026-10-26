import dotenv
import os
from openai import OpenAI

dotenv.load_dotenv()

llm = OpenAI(
    api_key=os.getenv('GROQ_API_KEY'),
    base_url="https://api.groq.com/openai/v1"
)


def bot(message):
    respone = llm.chat.completions.create(
        model='openai/gpt-oss-120b',
        messages=[
            {'role': 'user', 'content': message}
        ],
        temperature=0.7,
        max_tokens=100,
    )

    return respone.choices[0].message.content

def chat():
    print("Welcome to the Chat Bot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = bot(user_input)
        print(f"Bot: {response}")

def main():
    chat()


if __name__ == '__main__':
    main()
