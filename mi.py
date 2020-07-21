import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
name="sam@gmail.com"
URL = r'https://haveibeenpwned.com/unifiedsearch/'
URL=URL+name.replace('@','%40')
print(URL)
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
result = requests.get(URL, headers=headers)
print(result.content.decode())