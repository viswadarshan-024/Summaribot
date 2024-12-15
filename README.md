

# **Summaribot - Document Summarization and Interactive Chatbot**

This project integrates document summarization and an interactive chatbot powered by Streamlit, Groq API, and the Hugging Face (HF) Inference API. The application allows users to upload documents, generate summaries, and ask questions based on the document content.

---

## **Features**

- **Document Upload**: Upload PDFs, Word documents, or text files.
- **Summarization**: Automatically generate concise summaries of uploaded documents.
- **Interactive Chat**: Ask questions based on document summaries, powered by **Groq API**.
- **History Tracking**: View and manage previous document summaries and chat interactions.
- **Clear Interface**: Simple and intuitive web UI built with **Streamlit**.

---

## **Directory Structure**

```bash
Summaribot/
├── app.py         # Main application file
├── summarizer.py  # Summarization module
├── chat.py        # Chat module integrated with Groq API
├── history.py     # History management module
├── utils.py       # Utility functions for file processing
└── uploads/       # Directory for storing uploaded files
```

### Run the Application:

To run the project, ensure the following dependencies are installed:
  ```bash
  streamlit
  groq
  pdfplumber
  python-docx
  requests
```

Install them using:
  ```bash
  pip install -r requirements.txt
  ```
Start the application:
  ```bash
  streamlit run app.py
  ```

---
## Use the Features

### Summarize Document
- Upload your document (PDF or Word format).
- The app generates a concise summary for you.

### Chat
- Ask questions related to the summarized document.
- Responses will appear in real-time, including code snippets if applicable.

### History
- View or manage your past interactions with the chatbot.

---

## Acknowledgments
- **Groq API:** Powering the chatbot with conversational AI.
- **Streamlit:** For building the interactive web interface.
- **Hugging Face Models:** For summarization via `facebook/bart-large-cnn`.

---

## License
This project is licensed under the [GPL-3.0 license](https://www.gnu.org/licenses/gpl-3.0.en.html).

---

## Contributing
Contributions are welcome! Here's how you can contribute:
- Open issues to report bugs or suggest features.
- Submit pull requests to improve the code or documentation.
