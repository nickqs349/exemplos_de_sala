def pont():
    pontos = int(input('quanto ponto você tem? '))

    if pontos >= 90:
        print("A")
    elif pontos >= 80:
        print("B")
    elif pontos >= 70:
        print("C")
    elif pontos >= 60:
        print("D") 
    else:
        print("F")    

pont()