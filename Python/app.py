from flask import Flask, request, jsonify
from flask_cors import CORS
from scraper import Scraper, parse_ardes, parse_emag, parse_technopolis

app = Flask(__name__)
CORS(app)

@app.route('/search', methods=['POST'])
def search():
    # Receive JSON data from front-end
    data = request.get_json()  
    keywords = data.get('keywords')
    
    if not keywords:
        return jsonify({"error": "No keywords provided"}), 400

    # Run the scrapers with the keywords
    scraper_results = run_scraper(keywords)
    
    return jsonify(scraper_results)

def run_scraper(keywords):
        results={}
        sites = {
        'ardes.bg': Scraper(base_url='https://ardes.bg/products?q=',
                            format_symbol='%20',
                            parse_function=parse_ardes),
        'emag.bg': Scraper(base_url='https://www.emag.bg/search/',
                           format_symbol='%20',
                           parse_function=parse_emag),
        'technopolis.bg': Scraper(base_url='https://www.technopolis.bg/bg/search/',
                                  format_symbol='%20',
                                  parse_function=parse_technopolis)
        }
    
        for site_name, scraper in sites.items():
            soup = scraper.get_data(keywords)
            if soup:
                all_products = scraper.parse(soup)
                filtered_products = [product for product in all_products if "Смартфон" in product.get("title", "")]
                results[site_name] = filtered_products
            else:
                results[site_name] = []

        return results

if __name__ == '__main__':
    app.run(debug=True)
