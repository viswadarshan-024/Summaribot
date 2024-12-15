import requests

SUMMARIZE_API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
HEADERS = {"Authorization": "Bearer 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"}

def summarize_text(text):
    payload = {"inputs": text}
    response = requests.post(SUMMARIZE_API_URL, headers=HEADERS, json=payload)
    response.raise_for_status()
    if response.status_code == 200:
        return response.json()[0]["summary_text"]
    else:
        raise Exception(f"Summarization Error: {response.text}")
