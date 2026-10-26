import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User_Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-language" : "en-US,en;q=0.5",
}

def fetch_website_content(url):
    if not url.startswith(("http://, https://")):
        url = "https://" + url
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return f"Error fetching the website: {e}"
    
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.title.string if soup.title else "No title found"
    
    for tag in soup(["script", "style", "header", "footer", "nav", "aside"]):
        tag.decompose()
        
    text = soup.get_text(separator="\n")
    return f"Title: {title}\n\n Page Content:\n{text}"