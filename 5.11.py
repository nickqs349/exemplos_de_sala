def main():
    print("---calculadora de quadrados---")
    n = float(input("qual o número?"))
    result = calcular_quadrado(n)
    print(f"o quadrado de{n} é {result}")


def calcular_quadrado(n):
    return n * n


main() 
