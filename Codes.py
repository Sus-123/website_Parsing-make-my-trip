import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl

import pandas as pd
import requests

# webscrapping learner
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = 'https://www.goibibo.com/sitemap-https.xml'
he = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
}
response=requests.get(url,headers=he)
soup=BeautifulSoup(response.text,'html.parser')
total_data=soup.findAll("loc")
hotel_array=[]
dts={

    'hotel_name':[],
    'hotel_address':[],
    'price_range':[],
    'country_name':[],
    'city_name':[],
    'hotel_rating':[],
    'hotel_review':[],
    #'amneties':[],
    # 'top_review':[],
}
k=0;
for data in total_data:
    str=data.text
    if (str.find("hotels")>0):
        hotel_array.append(str)
for data in hotel_array:
    get_data=requests.get(data)
    soup1=BeautifulSoup(get_data.text,'html.parser')
    get_url=soup1.findAll("loc")
    for url in get_url:
        hotels_data=requests.get(url.text)
        soup2=BeautifulSoup(hotels_data.text,'html.parser')
        hotel_name=soup2.find("h3",attrs={"itemprop":"name"})
        t=soup2.find('p',attrs={'class':'HotelCardstyles__CurrentPrice-sc-1s80tyk-26 ckALLt','itemprop':'priceRange'})
        s4=""
        j=0
        if j==0:
            try:
                s4=t.text
            except:
                s4=""
        hotel_address=soup2.find("span",attrs={"itemprop":"streetAddress"})
        hotel_rating=soup2.find("div",attrs={"itemprop":"aggregateRating"})
        hotel_review=soup2.find("span",attrs={"class":"UserReviewstyles__UserReviewTextStyle-sc-1y05l7z-4 UNLBr"})
        i=0
        s1=""
        s2=""
        for link in soup2.findAll("a",attrs={"itemprop":"item","class":"Breadcrumbstyles__BreadCrumbATagItemLink-ily95m-5 kTxYic"}):
            x=link.findAll('span')
            if i==0:
                try:
                   s1=(x[2].contents[0])
                except:
                    s1=""
            else:
                try:
                    s2=(x[2].contents[0])
                except:
                    s2=""
            i+=1

        dts['hotel_name'].append(hotel_name.text if hotel_name else '')
        dts['hotel_address'].append(hotel_address.text if hotel_address else '')
        dts['price_range'].append(s4)
        dts['hotel_rating'].append(hotel_rating.text[0:5] if hotel_rating else '')
        dts['hotel_review'].append(hotel_review.text if hotel_review else '')
        dts['country_name'].append(s1)
        dts['city_name'].append(s2)

        k=k+1
        if k>100:
            break
    if k>100:
        break

table = pd.DataFrame(dts, columns=['hotel_name','hotel_address','price_range','country_name','city_name','hotel_rating','hotel_review'])
table.index = table.index + 1
table.to_csv(f'my_albums.csv', sep=',', encoding='utf-8', index=False)
print(table)
