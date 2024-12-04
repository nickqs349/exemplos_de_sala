def main():
    num = int(input("Digite um número: "))

    pariade(num)

def pariade(num):
    if num % 2 == 0:
        print("número par")
    else:
        print("número impar")

main()