# privacy-hashtag-generator.py
import os, sys
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

niche = sys.argv[1] if len(sys.argv) > 1 else input("Privacy niche (e.g., web3 / data protection): ")
count = int(sys.argv[2]) if len(sys.argv) > 2 else 20

prompt = f"""Generate {count} hashtags focused on privacy for niche: {niche}

2026 trends: zk, data sov, anon, no-track
- Mix: broad (#Privacy), specific (#ZKProofsInFarcaster), long-tail (#AnonymousMintingOnBase)
- 4–6 with emojis if fitting (e.g., #PrivacyLock🔒)
- Sort: popular → niche
- One per line with #

Return list only."""

try:
    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.85,
        max_tokens=250
    )
    print("\nPrivacy Hashtags:\n")
    print(res.choices[0].message.content.strip())
except Exception as e:
    print(f"Error: {e}")
