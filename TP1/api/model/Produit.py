from pydantic import BaseModel, PositiveInt

class Produit(BaseModel):
    id: int
    name: str
    prix: float
    description: str
    stockRestant: PositiveInt

# external_data = {
#     'id': 123,
#     'name': 'A',
#     'prix': 15,
#     'description': 'ABC',
#     'stockRestant': 1,
# }

# user = Produit(**external_data)



# print(user.id)


# #> 123
# print(user.model_dump())