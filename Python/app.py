from flask import Flask, request, jsonify
import subprocess
from flask_cors import CORS
import json

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
    scraper_results = run_scrapers(keywords)
    
    return jsonify(scraper_results)

# parsing stdout output and creating dictionaries
def parse(output):
     lines = output.splitlines()
     products = []

     for i in range(0, len(lines), 3):
        if i + 2 < len(lines):
            name = lines[i].strip()
            price = lines[i + 1].strip()
            link = lines[i + 2].strip()
            product = {"name": name, "price": price, "link": link}
            products.append(product)

     return products



def run_scrapers(keywords):
        results={}
    
        # Running scraper scripts with the keywords as an argument
        result_ardes = subprocess.run(['python', 'ardes_scr.py', keywords], capture_output=True, text=True,encoding='utf-8')
        result_emag = subprocess.run(['python', 'emag_scr.py', keywords], capture_output=True, text=True,encoding='utf-8')
        result_technopolis = subprocess.run(['python', 'technopolis_scr.py', keywords], capture_output=True, text=True,encoding='utf-8')
        
        try:
            ardes_output = result_ardes.stdout
            a_out=parse(ardes_output)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from ardes_scr.py output: {e}")
        
        try:
            emag_output = result_emag.stdout
            e_out=parse(emag_output)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from ardes_scr.py output: {e}")

        try:
            technopolis_output = result_technopolis.stdout
            t_out=parse(technopolis_output)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from ardes_scr.py output: {e}")
        
        # creating dictionary where each member is a list of dictionaries(products) 
        results = {
            'ardes.bg': a_out,
            'emag.bg': e_out,
            'technopolis.bg': t_out
        }

        return results

if __name__ == '__main__':
    app.run(debug=True)
