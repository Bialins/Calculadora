print("Escolha a operacao:")
print("1. Adicao")
print("2. Subtracao")
print("3. Multiplicao")
print("4. Divisao")

escolha = input("Digite o numero da operacao (1/2/3/4): ")

if escolha in ['1', '2', '3', '4']:
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))

    if escolha == '1':
        resultado = num1 + num2
        print(f"{num1} + {num2} = {resultado}")

    elif escolha == '2':
        resultado = num1 - num2
        print(f"{num1} - {num2} = {resultado}")

    elif escolha == '3':
        resultado = num1 * num2
        print(f"{num1} * {num2} = {resultado}")

    elif escolha == '4':
        if num2 != 0:
            resultado = num1 / num2
            print(f"{num1} / {num2} = {resultado}")
        else:
            print("Erro! Divisao por zero.")

else:
    print("Escolha invalida!")