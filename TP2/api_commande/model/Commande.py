from pydantic import BaseModel

class Commande(BaseModel):
    id: int
    idClient: int
    description: str
    price: float
    purchaseDate: str