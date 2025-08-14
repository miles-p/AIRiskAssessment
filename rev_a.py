from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.responses.create(
    model="gpt-5-nano-2025-08-07",
    input="How many floors is the Empire State Building?",
    instructions="Respond only with what is necessary; A good answer is a short answer."
)

print(response.output_text)