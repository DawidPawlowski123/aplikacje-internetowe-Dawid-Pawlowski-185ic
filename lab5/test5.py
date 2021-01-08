import requests
from bs4 import BeautifulSoup

# Make a request
page = requests.get(
    "https://dawidblog123.herokuapp.com/"
)
soup = BeautifulSoup(page.content, "html.parser")

# Create top_items as empty list
all_links = []
all_paragraf = []

# Extract and store in top_items according to instructions on the left
links = soup.select("a")
print("Liczba linkow = ", len(links))
for ahref in links:
    text = ahref.text
    text = text.strip() if text is not None else ""

    href = ahref.get("href")
    href = href.strip() if href is not None else ""
    all_links.append({"href": href, "text": text})
    # paragrafy
    paragraf = soup.select("p")
print("Liczba paragrafow = ", len(paragraf))
for ptext in paragraf:
    text = ptext.text
    text = text.strip() if text is not None else ""

    all_paragraf.append({"text": text})

print(all_links)
print("/n")
print(all_paragraf)