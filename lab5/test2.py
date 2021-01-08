import requests
from bs4 import BeautifulSoup

# Make a request
page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/"
)
soup = BeautifulSoup(page.content, "html.parser")



# Create all_h1_tags as empty list
all_h1_tags = []

# Set all_h1_tags to all h1 tags of the soup
for element in soup.select("h1"):
    all_h1_tags.append(element.text)

# Create seventh_p_text and set it to 7th p element text of the page
#seventh_p_text = soup.select("p")[5].text

#print(all_h1_tags, seventh_p_text)

print(soup.ul.text)

for x in range(4, 7):
    seventh_p_text = soup.select("p")[x].text
    print(all_h1_tags, seventh_p_text)

    