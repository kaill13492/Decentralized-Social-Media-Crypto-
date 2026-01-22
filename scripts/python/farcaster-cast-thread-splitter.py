# farcaster-cast-thread-splitter.py
# Split long text into Farcaster thread (max ~300 chars per cast)

import sys
from dotenv import load_dotenv

load_dotenv()  # optional if you add LLM later

def split_to_thread(text, max_chars=280, min_chars_per_cast=40):
    lines = text.split('\n')
    casts = []
    current = ""
    
    for line in lines:
        if len(current) + len(line) + 1 <= max_chars:
            current += line + "\n"
        else:
            if current:
                casts.append(current.strip())
            current = line + "\n"
    
    if current:
        casts.append(current.strip())
    
    # Merge very short last pieces if needed
    while len(casts) > 1 and len(casts[-1]) < min_chars_per_cast:
        casts[-2] += "\n" + casts.pop()
    
    return casts

if __name__ == "__main__":
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
    else:
        text = sys.stdin.read().strip()
    
    if not text:
        print("No text provided.")
        sys.exit(1)
    
    thread = split_to_thread(text)
    
    print(f"Thread ready ({len(thread)} casts):\n")
    for i, cast in enumerate(thread, 1):
        print(f"{i}/{len(thread)}")
        print(cast)
        print("-" * 60)
