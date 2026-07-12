"""
Project 1: Rule-Based AI Chatbot
DecodeLabs Industrial Training Kit - Batch 2026

Goal:
    A simple rule-based chatbot that responds to predefined user inputs
    using dictionary (hash map) lookups instead of long if-elif chains.

Key Requirements covered:
    - Continuous input loop (while True)
    - Sanitization (lowercase + strip whitespace)
    - Knowledge base dictionary with 5+ intents
    - Fallback response for unknown inputs
    - Clean exit command (kill command)

Bonus Feature:
    - Order Status Lookup: the chatbot can answer "where is my order ORD200005"
      style questions by reading orders_data.csv (converted from the provided
      dataset) into a dictionary, giving true O(1) lookups -- the same
      Hash Map concept covered in the training slides.
"""

import csv
import os
import re


# ---------------------------------------------------------------------------
# PHASE 1: KNOWLEDGE BASE (Dictionary = Hash Map of intents -> responses)
# ---------------------------------------------------------------------------
RESPONSES = {
    "hello": "Hi there! Welcome to DecodeLabs Support Bot. How can I help you today?",
    "hi": "Hello! How can I assist you?",
    "how are you": "I'm just a bunch of if-else rules, but I'm running perfectly fine! 😄",
    "what is your name": "I'm DecodeBot, your friendly rule-based assistant.",
    "help": (
        "I can help you with:\n"
        "  - Greetings (hello, hi)\n"
        "  - Order status  -> type: order status ORD200005\n"
        "  - Company info  -> type: contact\n"
        "  - Say 'bye' or 'exit' to leave the chat"
    ),
    "contact": "You can reach DecodeLabs at decodelabs.tech@gmail.com or +91 89330 06408.",
    "thanks": "You're welcome! Happy to help.",
    "thank you": "You're welcome! Happy to help.",
}

# Words that end the chat loop (the "Kill Command")
EXIT_COMMANDS = {"bye", "exit", "quit", "goodbye"}

# Default fallback response when nothing matches
DEFAULT_RESPONSE = "I do not understand that yet. Type 'help' to see what I can do."

DATA_FILE = os.path.join(os.path.dirname(__file__), "orders_data.csv")


# ---------------------------------------------------------------------------
# PHASE 2: LOAD DATASET INTO A DICTIONARY (Bonus feature)
# ---------------------------------------------------------------------------
def load_orders(path):
    """Reads orders_data.csv and returns a dict: {OrderID: order_info_dict}."""
    orders = {}
    if not os.path.exists(path):
        return orders

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            order_id = row.get("OrderID", "").strip().upper()
            if order_id:
                orders[order_id] = row
    return orders


ORDERS = load_orders(DATA_FILE)


# ---------------------------------------------------------------------------
# PHASE 3: SANITIZATION
# ---------------------------------------------------------------------------
def sanitize(raw_input):
    """Cleans user input: lowercase + strip extra whitespace."""
    return raw_input.strip().lower()


# ---------------------------------------------------------------------------
# PHASE 4: INTENT HANDLING
# ---------------------------------------------------------------------------
def handle_order_status(user_input):
    """
    Detects a request like: 'order status ORD200005' or 'track ORD200005'
    Returns a response string, or None if this isn't an order-status request.
    """
    match = re.search(r"\bORD\d+\b", user_input.upper())
    if match is None:
        return None  # Not an order-status style query
    order_id = match.group(0)

    order = ORDERS.get(order_id)
    if order is None:
        return f"Sorry, I couldn't find any order with ID {order_id}."

    return (
        f"Order {order_id} -> Product: {order.get('Product')}, "
        f"Status: {order.get('OrderStatus')}, "
        f"Tracking No: {order.get('TrackingNumber')}, "
        f"Total: {order.get('TotalPrice')}"
    )


def get_response(user_input):
    """Main decision function: routes input to the correct handler."""
    # 1. Try the order-status bonus feature first
    order_reply = handle_order_status(user_input)
    if order_reply is not None:
        return order_reply

    # 2. Fall back to the rule-based dictionary lookup (O(1) lookup)
    return RESPONSES.get(user_input, DEFAULT_RESPONSE)


# ---------------------------------------------------------------------------
# PHASE 5: THE HEARTBEAT (Continuous Loop)
# ---------------------------------------------------------------------------
def main():
    print("=" * 55)
    print(" DecodeBot - Rule-Based AI Chatbot (Project 1)")
    print(" Type 'help' for options, or 'bye' to exit.")
    print("=" * 55)

    while True:
        raw_input_text = input("You: ")
        clean_input = sanitize(raw_input_text)

        if clean_input in EXIT_COMMANDS:
            print("Bot: Goodbye! Have a great day. 👋")
            break

        reply = get_response(clean_input)
        print(f"Bot: {reply}")


if __name__ == "__main__":
    main()
