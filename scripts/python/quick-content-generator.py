# quick-content-generator.py
import os
from dotenv import load_dotenv
from openai import OpenAI     # swap with groq / anthropic if preferred

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# client = Groq(api_key=os.getenv("GROQ_API_KEY"))   # example alternative

template_path = "prompts/instagram/reel-hook-3sec-2025.txt"

with open(template_path) as f:
    template = f.read()

topic   = input("Topic / niche / product: ")
audience = input("Target audience: ")
emotion  = input("Emotion to trigger in first 3s: ")

prompt = (template
    .replace("………………………………………………", topic)
    .replace("………………………………………", audience)
    .replace("……………", emotion))

response = client.chat.completions.create(
    model="gpt-4o-mini",                # or claude-3-5-sonnet-latest / gemini-2.0-flash etc.
    messages=[{"role": "user", "content": prompt}],
    temperature=0.92,
    max_tokens=600
)

print("\n" + "═" * 70 + "\n")
print(response.choices[0].message.content.strip())
print("\n" + "═" * 70)
