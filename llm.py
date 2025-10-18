import os
from openai import OpenAI

# ---------- SETUP ----------
# Ollama is running at http://127.0.0.1:11434 by default.
client = OpenAI(
    base_url="http://127.0.0.1:11434/v1",   # <-- local Ollama
    api_key="ollama",                       # dummy – required by SDK, not used
)

MODEL = "gpt-oss:20b-cloud"   # change if your name differs

# ---------- CHAT LOOP ----------
print(f"🗨️  Chatting with {MODEL}. Type 'quit' to exit.\n")

conversation = [
    {"role": "system", "content": "You are a helpful assistant."}
]

while True:
    inp = input("\nYou: ")
    if inp.lower() == "quit":
        print("\nGood‑bye!")
        break

    # append user message
    conversation.append({"role": "user", "content": inp})

    try:
        resp = client.chat.completions.create(
            model=MODEL,
            messages=conversation,
        )
        # the assistant reply is in the first choice
        reply = resp.choices[0].message.content
        print(f"\nAI: {reply}")
        # keep the assistant message in history for continuity
        conversation.append({"role": "assistant", "content": reply})
    except Exception as exc:
        print(f"❌  Error: {exc}")
