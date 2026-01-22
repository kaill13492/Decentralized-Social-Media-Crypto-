# batch-farcaster-prompt-runner.py
# Improvement: batch multiple prompts, save outputs to files

import os, json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

prompt_files = ["prompts/farcaster/privacy-cast-thread.txt", "prompts/farcaster/zk-proof-frame-concept.txt"]  # add your paths
replacements = {"………………………………………………": "ZK in daily casts"}  # dict of placeholders to values

outputs = {}
for file in prompt_files:
    with open(file) as f:
        template = f.read()
    prompt = template
    for placeholder, value in replacements.items():
        prompt = prompt.replace(placeholder, value)
    
    try:
        res = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.9,
            max_tokens=800
        )
        outputs[file] = res.choices[0].message.content.strip()
    except Exception as e:
        outputs[file] = f"Error: {e}"

# Save to JSON (improvement for reuse/privacy – no cloud upload)
with open("outputs/batch_results.json", "w") as f:
    json.dump(outputs, f, indent=2)

print("Batch done! Check outputs/batch_results.json")
