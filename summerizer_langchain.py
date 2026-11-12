import os

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from scraper import fetch_website_content

load_dotenv()

promt = ChatPromptTemplate.from_template(
    "Give a short, friendly summary of the following website content in {language}. Ignore navigation links, ads, and other non-content elements. Focus on the main content of the page.\n\n{website_content}")

model = ChatOpenAI(
    model_name="openai/gpt-oss-20b",
    temperature=0.3,
    api_key=os.getenv("API_KEY_GROQ"),
    base_url="https://api.groq.com/openai/v1",
)

parser = StrOutputParser()

chain = promt | model | parser

def summarize_website(url):
    return chain.invoke({"website_content": fetch_website_content(url), "language": "Hindi"})

print(summarize_website("github.com"))