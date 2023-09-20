from curl_cffi import requests
from bs4 import BeautifulSoup
import json

def get_products_amazon(results):
    products = []

    for single in results[5:]:
        discount = single.find(class_="a-row a-size-base a-color-base").find_all('span')[-1]
        if(len(discount)==0):
            continue
        else:
            discount = discount.text
        name = single.find(class_="a-size-base-plus a-color-base a-text-normal").text
        url = "https://www.amazon.in"+single.find(class_="a-link-normal s-no-outline")['href']
        image_link = single.find(class_="s-image")['src']
        price = single.find(class_="a-price-whole").text
        


        products.append({"prod_name":name,
                         "prod_url":url,
                         "prod_image":image_link,
                         "prod_price":price,
                         "prod_discount":discount
                         })
              
    return products

def get_products_amazon2(results):
    products = []

    for single in results:
        discount = single.find(class_="a-row a-size-base a-color-base").find_all('span')[-2]
        if(len(discount)==0):
            continue
        else:
            discount = discount.text
        name = single.find(class_="a-size-medium a-color-base a-text-normal").text
        url = "https://www.amazon.in"+single.find(class_="a-link-normal s-no-outline")['href']
        image_link = single.find(class_="s-image")['src']
        price = single.find(class_="a-price-whole").text
        products.append({"prod_name":name,
                 "prod_url":url,
                 "prod_image":image_link,
                 "prod_price":price,
                 "prod_discount":discount
                 })
    return products
        
    



def scrap_amazon(category):
    url = f"https://www.amazon.in/s?k={category}"
    # headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"}
    resp = requests.get(url,impersonate="chrome110")
    soup = BeautifulSoup(resp.text,'html.parser')
    res_type = 1
    
    results = soup.find_all(class_='s-card-container s-overflow-hidden aok-relative puis-expand-height puis-include-content-margin puis puis-v32s3p1fquq4652buqesabfpl6j s-latency-cf-section s-card-border')
    
    if(len(results)==0):
        results = soup.find_all(class_="s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis puis-v32s3p1fquq4652buqesabfpl6j s-latency-cf-section s-card-border")
        resp=2


    if(results==None):
        return []
    else:
       if(resp==2):
           product_list = get_products_amazon2(results)
       else:
           product_list = get_products_amazon(results)
       
    return product_list



def scrap_flipkart(category):
    pass