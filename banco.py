menu = """
    Olá Seja bem vindo! Escolha uma opção abaixo:
    
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair
    
=> """

saldo = 0
limite = 500
extratoS = []
extratoD = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        print("Bem vindo! Vamos começar!\n")
        depositar = float(input("Informe o valor para depositar: R$ \n"))

        if depositar < -1:
            print("Valor inválido, informe um saldo positivo para deposito")
        else:
            print(f"O valor depositado foi: R${depositar}")

            saldo += depositar
            extratoD.append(depositar)

            print(f"Seu saldo atual é de R${saldo}")

    if opcao == "2":
        print("Bem Vindo! Vamos começar!\n")
        sacar = float(input("Informe um valor para sacar: R$ \n"))

        if sacar > 500:
            print("Informe um valor inferior a R$500,00 reais")

        elif saldo == 0 or saldo < sacar or sacar <= -0:
            print(f"Saldo insuficiênte para saque.")

        elif LIMITE_SAQUES == 0:
            print("Você atingiu seu limite diario de saque, vonte amanhã para sacar mais dinheiro!")

        else:
            saldo -= sacar
            LIMITE_SAQUES -= 1
            print(f"O valor sacado foi de R${sacar}. \nSeu saldo atual é de {saldo}")
            extratoS.append(sacar)

    if opcao == "3":

        if extratoS == [] and extratoD == []:
            print("Não foram realizadas movimentações nas contas")
            print(f"Seu saldo atual é de R${saldo:.2f}\n")
        else:
            print("##########   EXTRATO   ##########\n")
            print(f"Seus valores de saque foram: R${extratoS}")
            print(f"Seus valores de deposito foram: R${extratoD}\n")

            print(f"Seu saldo atual é de R${saldo:.2f}\n")
            print("#################################")

    if opcao == "4":
        print("Obrigado por usar nossos serviços!")
        break
else:
    print("Valor informado inválido.")