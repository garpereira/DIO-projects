# Descrição da tarefa:
# Desafio:
# Fomos contratados por um grande bano para desenvolver o seu novo sistema. Esse baco
# deseja modernizar suas operações e para isso escolheu a linguagem Python.
# Para a primeira versão do sistema devemos implementar apenas 3 operações
# - Depósito
# - Saque
# - Extrato

# Operação de depósito
# Deve ser possível depositar valores positivos para a conta bancária. A v1 do projeto trabalha
# apenas com um usuário, dessa forma não precisamos nos preocupar em identificar qual
# é o número da agência e da conta bancária. Todos os depósitos devem ser armazenados
# em uma variável e exibidos na operação de extrado

# Operação de Saque
# O sistema deve permitir realizar até 3 saques diários com o limite máximo de R$ 500,00 por saque
# Caso o usuário não tenha saldo em conta, o sistema deve exibir uma meensagem informando que não será
# possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável
# e exibidos na operação de extrato.

# Operação de Extrato
# Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser
# exibido o saldo atual da conta.
# Os valores devem ser exibidos utilizando o formato R$ 1000.00

extrato = {
    'deposito': [],
    'saque': [],
    'saldo': 0.00,
    'limite_saque': 0
}
while True:
    print("|=== Sistema Bancário ===|")
    print(f"Saldo disponível: {extrato['saldo']:.2f}")
    print("1 - Depósito \n2 - Saque \n3 - Extrato \n4 - Sair")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        valor = float(input('Digite o valor do depósito: '))
        while valor <= 0.00:
            print('Valor inválido. Tente novamente.')
            valor = float(input('Digite o valor do depósito: '))
        extrato['deposito'].append(valor)
        extrato['saldo'] += valor
        print(f'Depósito de R$ {valor:.2f} realizado com sucesso.\n')
    elif opcao == 2:
        if extrato['limite_saque'] == 3:
            print("Não é possível realizar novos Saques. Limite de saques diários atingido.\n")
        else:
            valor = float(input('Digite o valor do saque: '))
            while valor <= 0.00 or valor > 500.00:
                print('Valor inválido. Digite um valor maior que zero e menor que 501.')
                valor = float(input('Digite o valor do saque: '))
            if valor > extrato['saldo']:
                print(f"Saldo {extrato['saldo']:.2f} insuficiente para o saque de {valor:.2f}\n")
            else:
                extrato['saque'].append(valor)
                extrato['saldo'] -= valor
                extrato['limite_saque'] += 1
                print(f"Saque diário nro {extrato['limite_saque']}/3 no valor de R${valor:.2f} realizado com sucesso.\n")
    elif opcao == 3:
        print('---Extrato Bancário---')
        print(10*"=")
        print(10*"=")
        print('|Depósitos|')
        for d in extrato['deposito']:
            print(f"- {d:.2f}")
        print(10*"=")
        print(10*"=")
        print("|Saques|")
        for s in extrato['saque']:
            print(f"- {s:.2f}")
        print(10*"=")
        print(10*"=")
        print(f"Saldo disponível: {extrato['saldo']:.2f}")
    elif opcao == 4:
        print("Encerrando o programa...\nPrograma encerrado.")
        break
    else:
        print("Digite uma opção válida.\n")
        