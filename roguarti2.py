estudantes = [
    {"nome": "Hermione", "casa": "Griffinória", "patrono": "lontra"},
    {"nome": "Harry", "casa": "Griffinória", "patrono": "Veado"},
    {"nome": "Rony", "casa": "Griffinória", "patrono": "Jack Russell Terrier"},  
    {"nome": "Draco", "casa": "Sonerina", "patrono": None}
]

for estudante in estudantes:
    print(estudante["nome"], estudante["casa"], estudante["patrono"], sep=", ")