from pymongo import MongoClient

client = MongoClient("mongodb://bdd:27017/")
validation = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["id", "name", "prix", "description", "stockRestant"],
        "properties": {
            "id": {
                "bsonType": "int"
            },
            "name": {
                "bsonType": "string"
            },
            "prix": {
                "bsonType": "double"
            },
            "description": {
                "bsonType": "string"
            },
            "stockRestant": {
                "bsonType": "int"
            }
        }
    }
}

db = client['carPart']
try:
    db.create_collection(
        'produit',
        validator=validation,
        validationAction="warn"  # Options: 'warn' ou 'error' (en cas d'erreur de validation)
    )
except:
    print("collection already exists")