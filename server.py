from flask import Flask, request
import json
from mock_data import catalog
from config import db
from flask_cors import CORS

app = Flask("server")
CORS(app) # disable CORS to allow requests from any origin    

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
    cursor = db.prodcuts.find({})
    results = []
    for prod in cursor:
        prod ["_id"] = str(prod["_id"])
        results.append(prod)

    return json.dumps(results)    


# save products
@app.post("/api/catalog")
def save_prodcuts():
    product = request.get_json()
    db.prodcuts.insert_one(product)

    product["_id"] = str(product["_id"])

    return json.dumps(product)


@app.get("/api/catalog/<category>")
def get_by_category(category):
    cursor = db.prodcuts.find({"Category":category})
    result = []
    for prod in cursor:
        prod ["_id"] = str(prod["_id"])
        result.append(prod)

    return json.dumps(result)    



@app.get("/api/catalog/search/search/<title>")
def search_by_title(title):
    cursor = db.prodcuts.find({"title": {"$regex": title, "$options": "i"} }) 
    result = []
    for prod in cursor:
        prod ["_id"] = str(prod["_id"])
        result.append(prod)

    return json.dumps(result)            




@app.get('/api/product/cheaper/<price>')
def search_by_price(price):
    cursor = db.prodcuts.find({})
    result = []
    for prod in cursor:
        if prod ["price"] < float (price):
           prod["_id"] = str(prod["_id"])
           result.append(prod)

    return json.dumps(result)     


@app.get("/api/product/count")
def count_product():
    count = db.prodcuts.count_documents({})

    return json.dumps(count)



@app.get("/api/product/cheapest")
def get_cheapest():
    cursor = db.prodcuts.find({})
    answer = cursor[0]
    for prod in cursor:
        if prod ["price"]< answer["price"]:
            answer = prod

    answer["_id"] = str(answer["_id"])        
    return json.dumps(answer)


@app.get('/test/numbers')
def get_numbers():
 result = []
 for n in range (1,21):
     if n != 13 and n !=17:
        result.append(n)

 return json.dumps(result)




app.run(debug=True)