import requests
from bs4 import BeautifulSoup
import json

def get_products_amazon(results):
    products = []
    count = 0
    for single in results:
        name = single.find(class_="_cDEzb_p13n-sc-css-line-clamp-3_g3dy1").text
        url = "https://www.amazon.in"+single.find(class_="a-link-normal")['href']
        image_link = single.find(class_="a-section a-spacing-mini _cDEzb_noop_3Xbw5").contents[0]['src']
        products.append({"prod_name":name,
                         "prod_url":url,
                         "prod_image":image_link
                         })
                         
    return products



def scrap_amazon(category):
    url = f"https://www.amazon.in/gp/bestsellers/{category}"
    headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"}
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text,'html.parser')

    results = soup.find_all(id='gridItemRoot')

    if(results==None):
        return []
    else:
       product_list = get_products_amazon(results)

       return product_list


def scrap_flipkart(category):
    pass