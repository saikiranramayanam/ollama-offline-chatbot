import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"


def query_ollama(prompt):
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        return response.json()['response'].strip()
    except Exception as e:
        return f"Error: {e}"


# Load prompt templates
with open("prompts/zero_shot_template.txt", "r") as f:
    zero_template = f.read()

with open("prompts/one_shot_template.txt", "r") as f:
    one_template = f.read()


# ✅ 20 adapted e-commerce queries
queries = [
    "Where is my order?",
    "How do I return a product?",
    "My discount code is not working",
    "How can I track my shipment?",
    "I received a damaged product",
    "Can I cancel my order?",
    "What is your refund policy?",
    "How long does delivery take?",
    "Do you offer cash on delivery?",
    "How do I change my address?",
    "I didn't receive confirmation email",
    "Can I exchange my item?",
    "Payment failed but money deducted",
    "How to contact support?",
    "Is this product available?",
    "How to apply coupon?",
    "Order shows delivered but not received",
    "Can I return without invoice?",
    "How long for refund?",
    "My order is delayed"
]


# Write results
with open("eval/results.md", "w", encoding="utf-8") as f:

    f.write("# Chatbot Evaluation Results\n\n")

    f.write("| Query # | Customer Query | Prompt Type | Response | Relevance | Coherence | Helpfulness |\n")
    f.write("|--------|----------------|-------------|----------|-----------|-----------|-------------|\n")

    for i, query in enumerate(queries, 1):

        print(f"Processing Query {i}...")

        # Zero-shot
        zero_prompt = zero_template.replace("{query}", query)
        zero_response = query_ollama(zero_prompt)

        f.write(f"| {i} | {query} | Zero-Shot | {zero_response} |  |  |  |\n")

        # One-shot
        one_prompt = one_template.replace("{query}", query)
        one_response = query_ollama(one_prompt)

        f.write(f"| {i} | {query} | One-Shot | {one_response} |  |  |  |\n")


print("✅ All results saved in eval/results.md")