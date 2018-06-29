import urllib.request
from bs4 import BeautifulSoup as bs

quote_page = 'https://pcpartpicker.com/guide/CtBD4D/budget-vr-gaming-build'

# # for loop
# data = []
# for pg in quote_page:
#     # query the website and return the html to the variable 'page'
#     page = urllib.request.urlopen(pg)
#
#     # patse the html using beautiful soup and store in variable 'soup'
#     soup = bs(page, 'html.parser')
#
#     # Take out the <div> of name and get its value
#     name_box = soup.find('h1', attrs={'class': 'name'})
#     name = name_box.text.strip() # strip() is used to remove starting and trailing
#
#     # get the index price
#     price_box = soup.find('div', attrs = {'class':'price'})
#     price = price_box.text
#
#     # save the data in a tuple
#     data.append((name, price))
#
# for n in data:
#     print(n[0], n[1])













# query the website and return the html to the variable 'page'
page = urllib.request.urlopen(quote_page)

# parse the html using beautiful soup and store in variable 'soup'
soup = bs(page, 'html.parser')

# Take out the <div> of name and get its value
name_box = soup.find('h1', attrs={'class': 'component-type tl'})

name = name_box.text.strip() # strip() is used to remove starting and trailing

print(name)

# # get the index prince
# price_box = soup.find('div', attrs = {'class': 'price'})
# price = price_box.text
# print(price)
