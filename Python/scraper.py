import requests  # type: ignore
from bs4 import BeautifulSoup  # type: ignore

class Scraper:
    def __init__(self, base_url, format_symbol, parse_function):
        self.base_url = base_url
        self.format_symbol = format_symbol
        self.parse_function = parse_function
    
    def format_searchterm(self, term):
        return term.replace(" ", self.format_symbol)
    
    def get_data(self, searchterm):
        url = f'{self.base_url}{self.format_searchterm(searchterm)}'
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to fetch data: {response.status_code}")
            return BeautifulSoup('', 'html.parser')
        
        return BeautifulSoup(response.text, 'html.parser')
    
    def parse(self, soup):
        return self.parse_function(soup)
    

    
def parse_ardes(soup):
        prod_list = []
        results = soup.find_all('div', {"class": "product"})
        for item in results:
            try:
                product = {
                    'title': item.find('div', {"class": "isTruncated"}).text,
                    'price': float(item.find('span', {"class": "price-num"}).text[:-4] + '.' + item.find('sup', {"class": "price-sup"}).text),
                    'link': 'https://ardes.bg/' + item.find('a')['href']
                }
                prod_list.append(product)
            except (AttributeError, ValueError) as e:
                print(f"Error parsing item on ardes.bg: {e}")
                continue

        return prod_list

def parse_emag(soup):
        prod_list = []
        results = soup.find_all('div', {"class": "card-v2-wrapper js-section-wrapper"})
        for item in results:
            try:
                price_str = item.find('p', {"class": "product-new-price"}).get_text().replace('.', '').replace(',', '')
                price_num = ''.join(filter(str.isdigit, price_str))
                product = {
                    'title': item.find('a', {"class": "card-v2-title semibold mrg-btm-xxs js-product-url"}).get_text(),
                    'price': float(price_num) / 100 if price_num else 0,
                    'link': item.find('a')['href']
                }
                prod_list.append(product)
            except (AttributeError, ValueError) as e:
                print(f"Error parsing item on emag.bg: {e}")
                continue

        return prod_list

def parse_technopolis(soup):
        prod_list = []
        results = soup.find_all('te-product-box')
        for item in results:
            try:
                product = {
                    'title': item.find('h3', {"class": "product-box__title"}).text,
                    'price': float(item.find('span', {"class": "product-box__price-value"}).text),
                    'link': 'https://www.technopolis.bg/' + item.find('a', {"class": "product-box__title-link"})['href']
                }
                prod_list.append(product)
            except (AttributeError, ValueError) as e:
                print(f"Error parsing item on technopolis.bg: {e}")
                continue

        return prod_list

