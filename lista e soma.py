def somar_lista(lista):
    return numero1 + numero2 + numero3
if __name__ == "__main__":
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    numero3 = int(input("Digite o terceiro número: "))
    resultado = somar_lista([numero1, numero2, numero3])
    print(f"A soma dos números {numero1}, {numero2} e {numero3} é {resultado}.")