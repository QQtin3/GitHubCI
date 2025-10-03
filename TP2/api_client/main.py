import mysql.connector
from fastapi import FastAPI
from model.Client import Client
import os

app = FastAPI()

def get_db_connection():
    return mysql.connector.connect(
        host = os.getenv("HOST"),
        user= os.getenv('USER'),
        password= os.getenv('PASSWORD'),
        database=os.getenv('DATABASE')
    )

@app.get("/")
async def APIisRunning():
    return {"message": "API is running!"}


@app.get("/client/{id}")
async def get_client(id: int):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clients WHERE id = %s", (id,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()

    if row:
        return {"message": row}
    else:
        return {"message": "Client introuvable"}


@app.post("/client")
async def post_client(client: Client):
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO clients (firstName, lastName, email) VALUES (%s, %s, %s)"
    values = (client.firstName, client.lastName, client.email)
    cursor.execute(sql, values)
    conn.commit()
    new_id = cursor.lastrowid
    cursor.close()
    conn.close()

    return {"message": "Client créé", "id": new_id}


@app.put("/client/{id}")
async def update_client(id: int, client: Client):
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "UPDATE clients SET firstName = %s, lastName = %s, email = %s WHERE id = %s"
    values = (client.firstName, client.lastName, client.email, id)
    cursor.execute(sql, values)
    conn.commit()
    affected_rows = cursor.rowcount
    cursor.close()
    conn.close()

    if affected_rows == 0:
        return {"message": "Client introuvable"}

    return {"message": "Client mis à jour", "id": id}


@app.delete("/client/{id}")
async def delete_client(id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM clients WHERE id = %s"
    cursor.execute(sql, (id,))
    conn.commit()
    affected_rows = cursor.rowcount
    cursor.close()
    conn.close()

    if affected_rows == 0:
         return {"message": "Client introuvable"}

    return {"message": "Client supprimé", "id": id}