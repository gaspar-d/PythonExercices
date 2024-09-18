saldo = 0.0

MENU = """
[d] depositar
[s] sacar
[e] extrato
[q] sair
"""
while True:

    print(MENU)
    opcao = input("Escolha uma opção: ")

    if opcao.lower() == "d":
        print("deposito")
        deposito = float(input("Quanto deseja depositar? "))
        saldo += deposito

    elif opcao.lower() == "s":
        print("sacar")
        sacar = float(input("Quanto deseja sacar? "))
        saldo -= sacar

    elif opcao.lower() == "e":
        print(f"extrato{saldo}")

    elif opcao.lower() == "q":
        break

    else:
        print("Opção inválida")
