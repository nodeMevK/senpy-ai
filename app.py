import anthropic
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_KEY")
)

#print(os.getenv("ANTHROPIC_KEY"))

message = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=1000,
    temperature=0,
    system="You are a world-class poet. Respond only with short poems.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Why is the ocean salty?"
                }
            ]
        }
    ]
)
print(message.content)