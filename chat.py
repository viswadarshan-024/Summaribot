import os
from groq import Client

# Initialize the Groq client
client = Client(api_key="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")

# Define the chat model to be used (replace with a valid model name)
MODEL_NAME = "llama3-70b-8192"  

def chat_with_document(user_query, document_summary):
    """
    Use the document summary and user query to generate a conversational response using Groq API.
    """
    messages = [
        {
            "role": "system",
            "content": "You are an assistant that helps summarize documents and answer questions about them."
        },
        {
            "role": "user",
            "content": f"The document summary is as follows:\n{document_summary}\n\nUser Query: {user_query}"
        },
    ]

    try:
        # Make the API call to chat completion
        chat_completion = client.chat.completions.create(
            messages=messages,
            model=MODEL_NAME,
        )
        
        # Extract the assistant's response
        assistant_response = chat_completion.choices[0].message.content
        # assistant_response = chat_completion.get("choices")[0]["message"]["content"]
        return assistant_response

    except Exception as e:
        raise RuntimeError(f"Error while interacting with the Groq API: {str(e)}")
