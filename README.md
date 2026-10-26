# AI Website Summarizer

This project takes a website URL, extracts the readable content, and uses an LLM to generate a concise summary.

## Tech Stack

- Python
- Gradio
- BeautifulSoup
- Requests
- OpenAI Python SDK
- Groq API

## Setup

1. Open a terminal in the project folder.
2. Create a `.env` file in the project root.
3. Add your Groq API key in the `.env` file:

```env
API_KEY_GROQ=your_groq_api_key_here
```

4. Install all dependencies:

```bash
pip install -r requirements.txt
```

5. Run the app:

```bash
python app.py
```

6. Open the local Gradio URL shown in the terminal.

## Notes

- The `.env` file is ignored by Git and should never be committed.
- Make sure your Groq API key is valid and that the model name in `summerizer.py` is available to your account.
- If you get a 400 or 404 error, check the model name and the length of the webpage content being sent.

## Project Files

- `app.py` – Gradio app entry point
- `scraper.py` – fetches and cleans website content
- `summerizer.py` – calls the LLM and returns the summary
