from langchain_mistralai.chat_models import ChatMistralAI
from langchain_core.messages import HumanMessage

from langchain_community.document_loaders import AsyncChromiumLoader
from langchain_community.document_transformers import BeautifulSoupTransformer
import os
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from templates import JSON_TEMPLATE, PROMPT_MISTRAL
import json
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests
import time

load_dotenv()

## Model init

model = "mistral-large-latest"

client = MistralClient(api_key=os.environ["MISTRAL_KEY"])

## Functions


def get_one_page(url: str) -> str:
    # loader = AsyncChromiumLoader([url])
    # html = loader.load()
    start = time.time()
    # # To string
    # bs_transformer = BeautifulSoupTransformer()
    # docs_transformed = bs_transformer.transform_documents(html)
    # content = docs_transformed[0].page_content
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    text = soup.get_text()
    content = text
    stop = time.time()
    print(stop - start)
    return content


def extract_links(soup, base_url):
    links = set()
    for a_tag in soup.find_all("a", href=True):
        href = a_tag["href"]
        full_url = urljoin(base_url, href)
        # Filter out external links and same page links
        if (
            urlparse(full_url).netloc == urlparse(base_url).netloc
            and full_url != base_url
        ):
            links.add(full_url)
    return links


def get_all_pages(url: str) -> str:
    visited = set()
    to_visit = set([url])
    all_text = ""

    while to_visit:
        current_url = to_visit.pop()
        if current_url in visited:
            continue
        visited.add(current_url)

        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        text = soup.get_text()
        clean_text = " ".join(text.split())
        all_text += clean_text + " "

        links = extract_links(soup, url)
        to_visit.update(links - visited)

    return all_text


def generate(url: str, one_page: bool = True):
    if one_page:
        website = get_one_page(url)
    else:
        website = get_all_pages(url)

    prompt = PROMPT_MISTRAL.format(website)
    messages = [ChatMessage(role="user", content=prompt)]
    chat_response = client.chat(
        model=model,
        # response_format={"type": "json_object"},
        messages=messages,
    )

    response = chat_response.choices[0].message.content
    # response = json.loads(response)
    return response
