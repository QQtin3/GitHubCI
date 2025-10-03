import mysql.connector
from fastapi import FastAPI
from model.Commande import Commande
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI()

def getDBconnection():
    return mysql.connector.connect(
        host = os.getenv("HOST"),
        user= os.getenv('USER'),
        password= os.getenv('PASSWORD'),
        database=os.getenv('DATABASE')
    )


@app.get("/")
async def APIisRunning():
    return {"message": "API is running!"}


@app.get("/commande/{id}")
async def get_commande(id: int):
    conn = getDBconnection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM commande WHERE id = %s", (id,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()

    if row:
        return {"message": row}
    else:
        return {"message": "Commande introuvable"}


@app.post("/commande")
async def post_commande(commande: Commande):
    conn = getDBconnection()
    cursor = conn.cursor()
    sql = "INSERT INTO commande (idClient, description, price, purchaseDate) VALUES (%s, %s, %s, %s)"
    values = (commande.idClient, commande.description, commande.price, commande.purchaseDate)
    cursor.execute(sql, values)
    conn.commit()
    inserted_id = cursor.lastrowid
    cursor.close()
    conn.close()

    return {"message": "Commande ajoutée", "id": inserted_id}


@app.put("/commande/{id}")
async def update_commande(id: int, commande: Commande):
    conn = getDBconnection()
    cursor = conn.cursor()
    sql = """
        UPDATE commande 
        SET idClient = %s, description = %s, price = %s, purchaseDate = %s 
        WHERE id = %s
    """
    values = (commande.idClient, commande.description, commande.price, commande.purchaseDate, id)
    cursor.execute(sql, values)
    conn.commit()
    affected_rows = cursor.rowcount
    cursor.close()
    conn.close()

    if affected_rows == 0:
        return {"message": "Commande introuvable"}

    return {"message": "Commande modifiée", "id": id}


@app.delete("/commande/{id}")
async def delete_commande(id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM commande WHERE id = %s"
    cursor.execute(sql, (id,))
    conn.commit()
    affected_rows = cursor.rowcount
    cursor.close()
    conn.close()

    if affected_rows == 0:
        return {"message": "Commande introuvable"}

    return {"message": "Commande suprimée", "id": id}