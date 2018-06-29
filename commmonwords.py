from bs4 import BeautifulSoup as bs
import requests
import csv

source = requests.get('https://en.wikipedia.org/wiki/Most_common_words_in_English').text

soup = bs(source, 'lxml')

txt_file = open('commonwords.txt', 'w')

div = soup.find('div', class_= 'mw-parser-output')
tables = div.find('table', class_ = 'wikitable')

txt_file.write('words = [')
word_list = tables.find_all('a', class_='extiw')
for word in word_list:
    if word_list.index(word) == len(word_list) -1:
        txt_file.write('\' %s \'' %(word.text))
        break
    txt_file.write('\' %s \',' %(word.text))

txt_file.write(']')
txt_file.close()
# for article in soup.find_all('article'):
#     headline = article.h2.a.text
#     print(headline)
#
#     summary = article.find('div', class_='entry-content').p.text
#     print(summary)
#
#     try:
#         vid_src = article.find('iframe', class_='youtube-player')['src']
#
#         vid_id = vid_src.split('/')[4]
#         vid_id = vid_id.split('?')[0]
#
#         yt_link = 'https://youtube.com/watch?v=%s' %(vid_id)
#
#     except Exception as e:
#         yt_link = None
#
#     print(yt_link)
#     print()
#
#
# csv_file.close()
