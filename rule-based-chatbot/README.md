# 🤖 Rule-Based AI Chatbot — Project 1 (DecodeLabs Industrial Training)

A simple **rule-based chatbot** built with pure Python `if-else` / dictionary
logic (no AI/ML models). This is Project 1 of the DecodeLabs "Artificial
Intelligence" Industrial Training Kit — Batch 2026.

## 📌 What This Project Does

- Runs in a **continuous loop**, chatting with the user until they type an exit command.
- **Sanitizes** input (lowercase + trims whitespace) before processing.
- Uses a **dictionary (hash map)** as the knowledge base for O(1) instant response lookups — instead of a slow `if-elif` ladder.
- Has a **fallback response** for anything it doesn't understand.
- **Bonus feature:** it can look up real order status from `orders_data.csv`
  (converted from the provided dataset) — e.g. type `order status ORD200005`.

## 📂 Project Structure

```
rule-based-chatbot/
├── app.py             # Main chatbot program
├── orders_data.csv    # Dataset used for the order-lookup bonus feature
├── requirements.txt   # Dependencies (none — stdlib only)
├── .gitignore
└── README.md
```

## ▶️ How to Run

1. Make sure Python 3.8+ is installed on your system.
2. Open terminal in the project folder.
3. Run:
   ```bash
   python app.py
   ```
4. Chat with the bot! Try:
   - `hello`
   - `help`
   - `order status ORD200005`
   - `contact`
   - `bye` (to exit)

## 🧠 Key Concepts Covered

| Concept | Where in code |
|---|---|
| Continuous input loop | `while True` in `main()` |
| Sanitization | `sanitize()` function |
| Dictionary-based intent matching (O(1)) | `RESPONSES` dict + `.get()` |
| Fallback / default response | `DEFAULT_RESPONSE` |
| Exit / kill command | `EXIT_COMMANDS` + `break` |
| Real dataset lookup (hash map) | `load_orders()` + `handle_order_status()` |

## ✨ Possible Extensions

- Add more intents to the `RESPONSES` dictionary.
- Add nested conditions for smarter, multi-step conversations.
- Give the bot a unique personality/tone.
- Connect it later to an LLM as a "guardrail layer" (as described in the training slides) — rule-based matches respond instantly, and anything unmatched gets passed to an LLM.

## 🏢 About

Built as part of the DecodeLabs Industrial Training Kit (Batch 2026).
Contact: decodelabs.tech@gmail.com | www.decodelabs.tech
