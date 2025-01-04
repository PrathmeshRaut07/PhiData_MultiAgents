import os
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the OpenAI client with Hyperbolic API
client = openai.OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.hyperbolic.xyz/v1"
)

# Create a chat completion
api_key=os.getenv("DEEPSEEK_API_KEY")
chat_completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hey Deepseek are you trained on Open AI data ?"},
    ],
    temperature=0.7,
    max_tokens=1024,
)

# Print the response
print(chat_completion.choices[0].message.content)