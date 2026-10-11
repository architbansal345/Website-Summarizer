import requests
from bs4 import BeautifulSoup

Headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
}

def fetch_data(url):
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    try:
        response = requests.get(url, headers=Headers , timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return f"Error fetching data: {e}"
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.string if soup.title else "No title found"
    for tag in soup(['script', 'style', 'head', 'title', 'meta', 'link']):
        tag.decompose()
    text = soup.get_text(separator="\n", strip=True)
    return {
        "title": title,
        "text": text
    }
