from flask import Flask, request
import json
from mock_data import catalog
from config import db

app = Flask("server")

@app.get("/")
def home():
    return "hello from flask"

@app.get("/test")
def test():
    return "this is another endpoint"
    

@app.get("/about")
def about():
    return "Manuel Bailey"

    ########################################################################
################################CATALAG API###############################################
###########################################################################

@app.get("/api/version")
def version():
    version = {
        "V":"V.1.0.1",
        "name":"Candy_firewall", 
        "yourzip": "your",  
    } 
    return json.dumps(version) 


@app.get("/api/catalog")
def get_catalog():
    return json.dumps(catalog)


# save products
@app.post("/api/catalog")
def save_prodcuts():
    product = request.get_json()
    db.prodcuts.insert_one(product)

    product["_id"] = str(product["_id"])

    return json.dumps(product)


@app.get("/api/catalog/<category>")
def get_by_category(category):
    result = []
    for prod in catalog:
        if prod["Category"].lower() == category.lower():
            result.append(prod)

    return json.dumps(result) 


@app.get("/api/catalog/search/search/<title>")
def search_by_title(title):
    result = []
    for prod in catalog:
        if title.lower() in prod["title"].lower():
            result.append(prod)  
    return json.dumps(result)            




@app.get('/api/product/cheaper/<price>')
def search_by_price(price):
    result = []
    for prod in catalog:
        if prod ["price"] < float (price):
           result.append(prod)

    return json.dumps(result)     


@app.get("/api/product/count")
def count_product():
    count = len(catalog)
    return json.dumps(count)



@app.get("/api/product/cheapest")
def get_cheapest():
    answer = catalog[0]
    for prod in catalog:
        if prod ["price"]< answer["answer"]:
            answer = prod     

    return json.dumps(answer)


@app.get('/test/numbers')
def get_numbers():
 result = []
 for n in range (1,21):
     if n != 13 and n !=17:
        result.append(n)

 return json.dumps(result)




app.run(debug=True)