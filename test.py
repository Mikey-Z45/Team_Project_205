from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from pprint import pprint

my_site = 'https://thespaces.com/'
# my_site2 = 'https://www.theguardian.com/us'

req = Request(
    my_site,
    headers={'User-Agent': 'Mozilla/5.0'}
)

html = urlopen(req)
# pprint(html.read())
bs_obj = BeautifulSoup(html.read(), 'lxml')

title = bs_obj.body.h1
# print(title.get_text())

# for link in bs_obj.findAll("a"):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])

title_list = bs_obj.findAll("h1", {"class": "post-title"})

for title in title_list:
    print(title.get_text())
