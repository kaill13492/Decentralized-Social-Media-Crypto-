# batch-hashtag-suggester.py
import os, sys
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

niche = sys.argv[1] if len(sys.argv) > 1 else input("Niche / topic: ")
count = int(sys.argv[2]) if len(sys.argv) > 2 else 25

prompt = f"""Generate {count} trending + evergreen hashtags for content in the following niche: {niche}

Rules 2025–2026:
- mix broad, medium and long-tail
- include 4–8 very specific / community hashtags
- max 1–2 branded if it makes sense
- no more than 2–3 emojis in total across all tags
- sort from most broad → most niche
- one tag per line, with # already included

Return only the list – nothing else."""

res = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.7,
    max_tokens=300
)

print("\nSuggested hashtags:\n")
print(res.choices[0].message.content.strip())
