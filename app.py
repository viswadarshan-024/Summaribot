import os
import streamlit as st
from summarizer import summarize_text
from history import save_history, load_history
from chat import chat_with_document
from utils import read_document, split_into_chunks

# Upload Directory
UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

# Main Menu
menu = st.sidebar.selectbox("Menu", ["Summarize Document", "Chat", "History"])

# Summarize Document
if menu == "Summarize Document":
    st.header("Upload and Summarize Document")
    uploaded_file = st.file_uploader("Upload a document (PDF, DOCX, TXT):", type=["pdf", "docx", "txt"])

    if uploaded_file is not None:
        # Save uploaded file
        file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())

        # Determine file type
        file_type = uploaded_file.name.split(".")[-1]

        try:
            # Extract content
            document_content = read_document(file_path, file_type)
            st.success("Document content extracted successfully!")

            # Split into chunks
            chunks = split_into_chunks(document_content)
            st.info(f"Document split into {len(chunks)} chunks for summarization.")

            # Summarize each chunk
            full_summary = []
            for chunk in chunks:
                summary = summarize_text(chunk)  # Call to summarization model
                full_summary.append(summary)

            # Combine summaries
            final_summary = " ".join(full_summary)
            st.success("Summary Generated!")
            st.write(final_summary)

            # Save history
            save_history({
                "type": "Document",
                "input": uploaded_file.name,
                "summary": final_summary
            })
        except Exception as e:
            st.error(f"Error: {e}")

# Chat Interface
elif menu == "Chat":
    st.header("Chat with Document")
    user_query = st.text_input("Enter your query:")
    document_summary = load_history()

    if user_query and document_summary:
        response = chat_with_document(user_query, document_summary)
        st.write(f"**AI Response:** {response}")

# History
elif menu == "History":
    st.header("Summary History")
    history = load_history()

    if history:
        for idx, entry in enumerate(history[::-1], start=1):
            with st.expander(f"Entry {idx}"):
                st.write(f"**Type:** {entry.get('type', 'Unknown')}")
                st.write(f"**Input:** {entry.get('input', 'N/A')}")
                st.write(f"**Summary:** {entry.get('summary', 'N/A')}")
    else:
        st.info("No history available.")
