from bs4 import BeautifulSoup as bs
from timeprice import sec
from timeprice import coins as cs
import requests, time

sec1 = time.time()

source = requests.get('https://coinmarketcap.com/').text

soup = bs(source, 'lxml')
table =  soup.find('table').tbody
coins = 0

answ = input('Difference?')
if answ == 'y':
    minu =  int((sec1-sec)/60)
    seg = (sec1-sec) % 60
    print((minu, seg))
    for coin in table.find_all('tr'):
        if coins == 13:
            break
        name = coin.find('a', class_='currency-name-container').text
        price = coin.find('a', class_='price').text
        price = float(price[1:])
        coins += 1
        difference = price - cs[str(name)]
        print(name.ljust(15, '.'), difference)
    coins = 0
    print('\n\n')

file = open('timeprice.py', 'w')
file.write('sec = %i\n' % (sec1))
file.write('coins = {')

for coin in table.find_all('tr'):
    if coins == 13:
        break
    name = coin.find('a', class_='currency-name-container').text
    price = coin.find('a', class_='price').text
    print(name.ljust(15, '.'), price)
    file.write("'%s':%s" % (name,price[1:]))
    if coin != 12:
        file.write(',')
    coins += 1
file.write('}')
file.close()


#     if (link.caption.string == 'State capitals of the United States'):
#         states = []
#         state = []
#         count = 0
#         for cell in link.find_all('td'):
#             state.append(cell.string)
#             count += 1
#             if count == 11:
#                 states.append(state)
#                 state = []
#                 count = 0
#
# text_file.write('state_capital = {')
# for state in states:
#     if states.index(state) != 0:
#         text_file.write(', ')
#     text_file.write("'%s' : ('%s', '%s')" % (state[0], state[1], state[3]))
#
# text_file.write('}')


# state_capital = {Alabama: (AL, Montgomery), Alaska: (AK, Juneau), Arizona: (AZ, Phoenix), Arkansas: (AR, Little Rock), California: (CA, Sacramento), Colorado: (CO, Denver), Connecticut: (CT, Hartford), Delaware: (DE, Dover), Florida: (FL, Tallahassee), Georgia: (GA, Atlanta), Hawaii: (HI, Honolulu), Idaho: (ID, Boise), Illinois: (IL, Springfield), Indiana: (IN, Indianapolis), Iowa: (IA, Des Moines), Kansas: (KS, Topeka), Kentucky: (KY, Frankfort), Louisiana: (LA, Baton Rouge), Maine: (ME, Augusta), Maryland: (MD, Annapolis), Massachusetts: (MA, Boston), Michigan: (MI, Lansing), Minnesota: (MN, Saint Paul), Mississippi: (MS, Jackson), Missouri: (MO, Jefferson City), Montana: (MT, Helena), Nebraska: (NE, Lincoln), Nevada: (NV, Carson City), New Hampshire: (NH, Concord), New Jersey: (NJ, Trenton), New Mexico: (NM, Santa Fe), New York: (NY, Albany), North Carolina: (NC, Raleigh), North Dakota: (ND, Bismarck), Ohio: (OH, Columbus), Oklahoma: (OK, Oklahoma City), Oregon: (OR, Salem), Pennsylvania: (PA, Harrisburg), Rhode Island: (RI, Providence), South Carolina: (SC, Columbia), South Dakota: (SD, Pierre), Tennessee: (TN, Nashville), Texas: (TX, Austin), Utah: (UT, Salt Lake City), Vermont: (VT, Montpelier), Virginia: (VA, Richmond), Washington: (WA, Olympia), West Virginia: (WV, Charleston), Wisconsin: (WI, Madison), Wyoming: (WY, Cheyenne)}
# div = soup.find('span', class_ = 'sidebar-price-widget-cbu-price ')
# print(div)
# tables = div.find('table', class_ = 'wikitable')
#
# txt_file.write('words = [')
# word_list = tables.find_all('a', class_='extiw')
# for word in word_list:
#     if word_list.index(word) == len(word_list) -1:
#         txt_file.write('\' %s \'' %(word.text))
#         break
#     txt_file.write('\' %s \',' %(word.text))
#
# txt_file.write(']')
# txt_file.close()
