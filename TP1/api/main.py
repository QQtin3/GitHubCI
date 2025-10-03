from fastapi import FastAPI
from model.Produit import Produit
from pymongo import MongoClient

client = MongoClient("mongodb://bdd:27017/")
app = FastAPI()

produitTable = client['carPart']['produit']

@app.get('/')
async def APIisRunning():
    return {"message": "API is running!"}

@app.get("/produit/{id}")
async def get_produit(id: int):
    data = produitTable.find_one({'id': id})
    return {"message": Produit(data)}

@app.post("/produit")
async def post_produit(produit: Produit):
    data = produitTable.insert_one(produit)
    return {"message": data}

@app.put("/produit")
async def update_produit(produit: Produit):
    data = produitTable.update_one(produit)
    return {"message": data}

@app.delete("/produit/{id}")
async def delete_produit(id: int, produit: Produit):
    data = produitTable.delete_one(produit)
    return {"message": data}