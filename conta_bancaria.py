menu = """

[d]Depositar
[s]Sacar
[e]Extrato
[p]Pix
[q]Quit

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
numero_pix = 0
LIMITE_PIX = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('Informe o valor de depósito: '))
        
        if valor > 0:
            saldo += valor
            extrato += f'C Depósito: R$ {valor:.2f}\n'
        else:
            print("Operação falhou! O valor informado é invalido.")
                
    elif opcao == 's':
        valor = float(input('Informe o valor de saque: '))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! Você não tem limite.")
        elif excedeu_saques:
            print("Operação falhou! Número de saques excedidos.")
        elif valor > 0:
            saldo -= valor
            extrato += f'S Saque: R$ {valor:.2f}\n'
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == 'e':
        print("***************EXTRATO***************\n")
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('\n')
        print('C = Creditado')
        print('T = Debitado')
        print('S = Debitado')
        print("*************************************")
    
    elif opcao == 'p':
        valor = float(input('Informe o valor da transferência: '))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_pix = numero_pix >= LIMITE_PIX

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! Você não tem limite.")
        elif excedeu_pix:
            print("Operação falhou! Número de transferências excedidos.")
        elif valor > 0:
            saldo -= valor
            extrato += f'T Transferência Pix: R$ {valor:.2f}\n'
            numero_pix += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == 'q':
        break

    else:
        print("Operação inválida, por favor selecione novamente a operção desejada.")


    
