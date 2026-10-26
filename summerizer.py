import os
from dotenv import load_dotenv
from openai import OpenAI
from scraper import fetch_website_content
load_dotenv()

client = OpenAI(
    api_key=os.getenv("API_KEY_GROQ"),
    base_url="https://api.groq.com/openai/v1"
)
system_prompt = """You analyze the contents of the website and provide
                friendly summary. Ignore navigation links, ads, and other non-content elements. 
                Focus on the main content of the page."""
def summarize_website(url):
    website  = fetch_website_content(url)
    website = website[:5000]
    response = client.chat.completions.create(
        model = "openai/gpt-oss-20b",
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Summerize the following website: \n\n{website}"},
        ],
    )
    return response.choices[0].message.content