# AI Content Factory – Tworzenie kodu i treści na social media

Repozytorium z promptami, skryptami i workflowami do masowego, ale sensownego tworzenia treści na Instagram, X/Twitter, LinkedIn, TikTok, YouTube Shorts i nie tylko – z pomocą LLM-ów (GPT-4o, Claude 3.5/4, Grok, Gemini, Llama 3.1/4, DeepSeek-R1 itp.).

## Co tu znajdziesz?

- **Najlepsze prompty** (ciągłe aktualizacje 2025/2026)
- Skrypty Python do generowania dziesiątek postów na raz
- Szablony brand voice i CTA
- Przykłady realnych kampanii (co zadziałało → viral)
- Generatory promptów pod grafikę (Flux, Midjourney v7, Ideogram 3.0, Recraft)

## Struktura
prompts/          → czysty prompt engineering
scripts/          → automatyzacja (OpenAI, Groq, Anthropic, Ollama...)
examples/         → realne case studies + wyniki
media/            → mockupy i gotowce graficzne
## Szybki start (Python)

1. Sklonuj repo

```bash
git clone https://github.com/TWOJA_NAZWA/AI-Content-Factory.git
cd AI-Content-Factorypython -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python scripts/python/generate_post.py --platform instagram --niche "e-commerce moda" --count 3
