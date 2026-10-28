from pyexpat.errors import messages

import dotenv
import os
from openai import OpenAI

dotenv.load_dotenv()





class ChatBot:
    def __init__(self):
        self.llm = OpenAI(
            api_key=os.getenv('GROQ_API_KEY'),
            base_url="https://api.groq.com/openai/v1"
        )

        self.messages = [
            {'role': 'system', 'content': '''you are a helpful assistant.
            Your name is neon_bot. in the first response, introduce yourself.give short and concise answer'''}
        ]

        self.total_tokens = 0

    def bot(self, message):

        self.messages.append({"role": "user", "content": message})

        respone = self.llm.chat.completions.create(
            model='openai/gpt-oss-120b',
            messages=self.messages,
            temperature=0.7,
            max_tokens=100,
        )

        response_message = respone.choices[0].message.content
        self.messages.append({"role": "assistant", "content": response_message})

        self.total_tokens += respone.usage.total_tokens

        return response_message


    def chat(self):
        print("Welcome to the Chat Bot! Type 'q' to quit.")
        while True:
            user_input = input("You: ")
            if user_input.strip().lower() == 'q':
                print("Goodbye!")
                break
            response = self.bot(user_input)
            print(f"Bot: {response}")

    def report(self):
        for message in self.messages:
            role = message['role']
            content = message['content']
            print(f"{role.capitalize()}: {content}")

        print(f'Total tokens consumed: {self.total_tokens}')


def main():
    bot = ChatBot()
    bot.chat()
    bot.report()


if __name__ == '__main__':
    main()
