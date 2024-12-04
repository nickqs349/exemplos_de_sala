p = str(input("diga o nome de um personagem")).title()

if p == "Harry P." or p ==  "Hermione G." or p == "Ron W.":
    print(f"A casa de {p} é Grifinoria")
elif p == "Draco M.":
    print(f"A casa de {p} é Sonserina")
elif p == "Luna L.":
    print(f"A casa de {p} é Corvinal")
elif p == "Cedric D.":
    print(f"A casa de {p} é Lufa-Lufa")
else:
    print("personagem não encontrado.")