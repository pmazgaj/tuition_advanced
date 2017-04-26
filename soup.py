import requests
from BeautifulSoup4 import BeautifulSoup as bs

request = requests.get("http://foo.bar")
soup = bs(request.text)
some_elements = soup.find_all("div", class_="myCssClass")
