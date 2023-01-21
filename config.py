import pymongo
import certifi

connection_str="mongodb+srv://WrittenByManny:Abcd1234@cluster0.szhhsgp.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(connection_str, tlsCafile=certifi.where())
db = client.get_database("OnlineStore")