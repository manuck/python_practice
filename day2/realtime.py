import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com/"

response = requests.get(url)


soup = BeautifulSoup(response.text, 'html.parser')


#key = soup.select('.ah_ro;ll')
#lists = key[0].select('.ah_k')  or  lists = key.select_one('.ah_k')
#for word in lists:
#    print(word.text)


rank =  soup.select('.ah_r')
keyword =  soup.select('.ah_k')
for i in range(0,20):
    print(rank[i].text +" = "+ keyword[i].text)
    

