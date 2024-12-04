x = float(input("digite um número: "))
y = float(input("digite um segundo número:"))

#calculos e o que vai mostrar no terminal.
print(f"a soma de {x} + {y} é {(x+y):_.2f}".replace(".",","))
print(f"a subtração de {x} + {y} é {(x-y):_.2f}".replace(".",","))
print(f"a divisão de {x}+{y} é {(x/y):_.2f}".replace(".",","))#round arredonda o valor para o inteiro.
print(f"a multiplicação de {x}+{y} é {(x*y):_.2f}".replace(".",","))
print(f"o resto de {x}+{y} é {x%y}".replace(".",","))
print(f"{x} elevado a {y} é {x ** y:,.2f}".replace(".",",").replace("_","."))
                
'''
r = x**y
r = f"{r :_.2f}"
print(r .replace(".",",").replace("_","."))
'''