import requests 
from bs4 import BeautifulSoup

odpowiedz = requests.get("https://pl.wikipedia.org/wiki/Zygmunt_III_Waza")
print("odpowiedz = \n", odpowiedz)
print(odpowiedz.status_code)
html_text: str = odpowiedz.text
#print("Strona o Wazie = \n", html_text)

user1 = requests.get("https://jsonplaceholder.typicode.com/users/1")
json_text: dict = user1.json()
print("url = ", user1.url)
print("json_text = ", json_text)
print("history = ", user1.history)

# print("odpowiedz tekstowa = \n", html_text)

html_doc = """<html>
<head>
    <title>Moja pierwsza strona!</title>
</head>
<body>
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec posuere elit at malesuada tempor. Donec eget ligula in ante auctor luctus. Phasellus iaculis porttitor gravida. Donec eget sem lorem. Morbi a libero imperdiet, viverra tellus ac, consequat tortor. Suspendisse nibh massa, accumsan non neque a, vestibulum commodo dui.</p>
<p>Phasellus vestibulum ut <br>erat sit amet ullamcorper. Nam at elit feugiat, dapibus ante vitae, ullamcorper dui. Nunc rutrum at nibh tincidunt mattis. In finibus sed ante vel mollis. Donec at semper metus. Aenean quis consectetur risus. Sed suscipit felis sed ex pretium euismod. In fermentum mi a odio porttitor, dapibus aliquet leo accumsan. Suspendisse pretium augue et faucibus euismod. Quisque risus metus, ultricies nec tortor at, efficitur convallis nunc.</p>
<ul>
    <li>Pierwszy punkt</li>
    <li>Drugi punkt</li>
    <li>Trzeci punkt</li>
</ul>
<ol>
    <li>Pierwszy punkt</li>
    <li>Drugi punkt</li>
    <li>Trzeci punkt</li>
</ol>
<table border="3" bgcolor="#ff00ff" class="tabela blog">
    <tr><th>Naglowek 1</th><th>Naglowek 2</th></tr>
    <tr><td>komorka 11</td><td>komorka 12</td></tr>
    <tr><td>komorka 21</td><td>komorka 22</td></tr>
</table>
<a href="http://google.pl">Arcyciekawa strona</a>
</body>
</html>"""


url_amw = "https://www.amw.gdynia.pl/"
# page = requests.get(url_amw)
# soup = BeautifulSoup(page.content, "html.parser")
soup = BeautifulSoup(html_doc, "lxml")

# Extract head of page
page_head = soup.head
print("Typ = ", type(page_head))

first_p = soup.select("p")[0].text
print("First p =\n", first_p)

another_p = soup.select("p")[1].text
print("Another p =\n", another_p)

print("Liczba zanacznikow 'p' = ", len(soup.select("p")))


# title
print("TITLE")
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.text)
print(soup.title.contents)
print("\n")

# ul
print("UL")
print(soup.ul.text)
print("\n")


# atrybuty
print("ATRYBUTY")
print(soup.table["border"])
print(soup.table.has_attr("border"))
print(soup.table.has_attr("href"))
print(soup.table.attrs)
print("\n")


# find
print("FIND")
print(soup.find_all("p"))
print(soup.find(border="3"))
print("Find klasy = ", soup.find(class_="tabela"))
print("Select klasy = ", len(soup.select("table.tabela")))
print(soup.find(href=True))
# print("Find src = \n", soup.find(src=False)) # be careful!

print("\n")

# next
print("NEXT")
print(soup.th.next_element)
print(soup.tr.next_sibling)
print(soup.tr.next_sibling.next_sibling)

