import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore
import sys

# creating correct search term from user keywords
def format_searchterm(term):
    technopolis_symbol = '%20'
    return term.replace(' ', technopolis_symbol)

# getting raw HTML from the site
def get_data(searchterm):
    url = f'https://www.technopolis.bg/bg/search/{searchterm}'
    req = requests.get(url)
    if req.status_code != 200:
        print(f"Failed to fetch data: {req.status_code}")
        return None
    soup = BeautifulSoup(req.text,'html.parser')
    return soup

# parsing the raw HTML and taking the needed information
def parse(soup):
    prod_list = []
    results = soup.find_all('te-product-box')
    for item in results:
        product = {
            'title': item.find('h3', {"class": "product-box__title"}).text,
            'price': float(item.find('span', {"class": "product-box__price-value"}).text),
            'link' : 'https://www.technopolis.bg/' + item.find('a', {"class": "product-box__title-link"})['href']
        }
        prod_list.append(product)
    
    return prod_list

# printing filtered data
def output(prod_list):
    sys.stdout.reconfigure(encoding='utf-8')
    filtered = [item for item in prod_list if "Смартфон" in item["title"].strip()]
    for key in filtered:
        for i in key:
             print(key[i])
    

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a search term.")
        sys.exit(1)

    searchterm = format_searchterm(sys.argv[1])
    soup = get_data(searchterm)
    productslist = parse(soup)
    output(productslist)



