from openai import OpenAI
from dotenv import load_dotenv
from scrapper import fetch_data
import os

load_dotenv()

system_prompt = """
You are a helpful assistant that summarizes websites.
You will be given a website and you will need to summarize it.
You will need to summarize the website in a way that is easy to understand and to the point.
"""
client = OpenAI(api_key=os.getenv("GROQ_API_KEY"),
base_url="https://api.groq.com/openai/v1")

def summarize_text(url):
    website = fetch_data(url)
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": website["text"]}
        ]
    )
    return response.choices[0].message.content
