from bs4 import BeautifulSoup
from sendemail import sendmsg
import requests
import time
import getpass

email = input('Enter your email: ')
password = getpass.getpass('Enter your password: ')

#Data that was already discovered (prevents duplicates)
cacheData = []

#Number of Repetitions and amount of found items
epoch = 0
finds = int(len(cacheData))
search = ['desk','Desk','frame','Frame','fridge','Fridge','computer', 'Computer', 'desktop','Desktop','mac','Mac']

def find(item):
    global epoch

    page_link = 'https://newyork.craigslist.org/search/zip'

    page_response = requests.get(page_link, timeout=5)

    page_content = BeautifulSoup(page_response.content, "html.parser")

    items_found = []

    separate_tags = page_content.find_all("a", attrs={'class' : 'result-title'})
    for a in separate_tags:
        for item in search:
            if item in a.text:
                x = {
                    'search': item,
                    'data-id': a['data-id'],
                    'title': a.text,
                    'link': a['href']
                }
                items_found.append(x)
            else:
                None
    setMessage(items_found)
    epoch += 1
    print('\nEpoch ' +str(epoch)+'\n--------------' )
    print('Found ' + str(len(items_found)) + '\nItem(s) Matching: ' + str(search))
    print('Cache Data: '+ str(cacheData))

    time.sleep(10)
    find(search)


def setMessage(items):
    message = []

    for each in items:
        if each['data-id'] not in cacheData:
            setting_msg = {
                'search': each['search'],
                'title': each['title'],
                'link': each['link']
            }
            message.append(setting_msg)
            cacheData.append(each['data-id'])
            
    if message:
        sendmsg(message, email, password)

def main():
    # search = str(input("Enter the item name: "))
    find(search)

if __name__ == '__main__':
    main()