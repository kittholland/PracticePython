from bs4 import BeautifulSoup
from requests import get
request = get("https://nytimes.com")
soup = BeautifulSoup(request.text, 'html.parser')
title_html = soup.find_all('h2', 'story-heading')
titles = [title.get_text() for title in title_html]
for title in titles:
    print(title)