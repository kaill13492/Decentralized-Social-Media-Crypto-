# farcaster-hashtag-and-frame-idea-generator.py
import os, sys
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

niche = sys.argv[1] if len(sys.argv) > 1 else input("Niche / topic for Farcaster: ")
count  = int(sys.argv[2]) if len(sys.argv) > 2 else 8

prompt = f"""Generate {count} creative Farcaster Frame / Mini App ideas for niche: {niche}

Each idea should be:
- One-sentence description
- Primary hook (what makes it viral/tappable)
- Suggested buttons (2–4)
- One strong hashtag combo (3–6 tags)

2025–2026 trends: onchain actions, streaks, quizzes, mints, polls, social loops, low-friction tx

Output format – one idea per block, no extra text.
Idea 1:
Description: …
Hook: …
Buttons: …
Hashtags: …
"""

res = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    temperature=1.0,
    max_tokens=900
)

print("\nFarcaster Frame Ideas:\n")
print(res.choices[0].message.content.strip())
