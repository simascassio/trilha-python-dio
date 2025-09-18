

print("Olá, Bem-vindo ao Banco Simas!")

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print("\nEscolha uma das opções abaixo: ")
    print("1 - Depositar")  
    print("2 - Sacar")
    print("3 - Extrato")
    print("4 - Sair")

    menu = input("Digite a opção desejada: ")

    if menu == "1":
        valor = float(input("Digite o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito realizado com sucesso! R$ {valor:.2f}")
        else:
            print("Valor inválido para depósito.")

    elif menu == "2":
        saque = float(input("Digite o valor do saque: "))
        
        if saque > saldo:
            print("Saldo insuficiente para saque.")
        elif saque > limite:
            print("Valor do saque excede o limite permitido por operação.")
        elif saque <= 0:
            print("Valor inválido para saque.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Número máximo de saques diários atingido.")
        else:
            saldo -= saque
            numero_saques += 1
            extrato += f"Saque: R$ {saque:.2f}\n"
            print(f"Saque realizado com sucesso! R$ {saque:.2f}")

    elif menu == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("==========================================")

    elif menu == "4":
        print("Obrigado por usar nosso sistema bancário. Até logo!")
        break

    else:
        print("Operação inválida, por favor selecione novamente.")

     

       
