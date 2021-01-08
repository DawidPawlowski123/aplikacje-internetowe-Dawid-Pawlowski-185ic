import requests
from bs4 import BeautifulSoup

# Make a request
page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/"
)
soup = BeautifulSoup(page.content, "html.parser")

# Create top_items as empty list
image_data = []

# Extract and store in top_items according to instructions on the left
images = soup.select("img")
print("Liczba obrazkow =", len(images))
for image in images:
    # print(type(image))
    src = image.get("src")
    alt = image.get("alt")
    image_data.append({"src": src, "alt": alt})

print(image_data)