inicio = """
    ** Banco PY **

    - Escolha a opção abaixo:

    [1] = Depósito
    [2] = Saque
    [3] = Extrato
    [4] = Saldo
    [0] = Sair

Digite a opção: """

saldo_bancario: float = 0
quantidade_saques = 0
lista_deposito = []
lista_saque = []

def saldo():
    global saldo_bancario
    return print(f"Seu saldo atualizado: R$ {saldo_bancario:.2f}.")

def deposito(valor: float):
    global saldo_bancario, lista_deposito
    saldo_bancario += valor
    lista_deposito.append(valor_depositado)
    return saldo()

def saque(saque: float):
    global saldo_bancario, lista_saque
    saldo_bancario -= saque
    lista_saque.append(valor_sacado)
    return saldo()

while True:
    operacao = input(inicio)
    
    if operacao == "1":
        valor_depositado = float(input("Qual o valor do depósito?: "))
        if valor_depositado <= 0:
            print("O valor informado é inválido.")
        else:
            print("Parabéns! Depósito realizado.")
            deposito(valor_depositado)
            

    elif operacao == "2":
        valor_sacado = float(input("Qual valor do saque?: "))
        if saldo_bancario <= valor_sacado:
            print("Saldo insuficiente")
            print(f"Seu saldo é de: R$ {saldo_bancario:.2f}.")
        elif quantidade_saques >= 3:
            print("OPS! Você atingiu o limite máximo de 3 saques diários.")
        elif valor_sacado > 500:
            print("OPS! O valor do saque excede o limite.")
        else:
            quantidade_saques += 1
            saque(valor_sacado)
            
            
    elif operacao == "3":
        print(''' **EXTRATOS** \n [1] Extrato de Depósito \n [2] Extrato de Saque \n''')
        extrato = input("Digite a opção desejada: ")

        if extrato == "1":
            if not lista_deposito:
                print("Não foram realizadas movimentações.")
            else:
                print("Extratos de Depósitos: ")
                for valor1 in lista_deposito:
                    print(f"R$ {valor1:.2f}")
        else:
            if not lista_saque:
                print("Não foram realizadas movimentações.")
            else:
                print("Extratos de Saques: ")
                for valor2 in lista_saque:
                    print(f"R$ {valor2:.2f}")

    elif operacao == "4":
        saldo()

    aguardar = input("Para realizar outra operação, pressione ENTER.")
