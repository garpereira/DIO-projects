    # Com os conhecimentos adquiridos de data e hora, fomos encarregados de implementar as seguintes funcionalidades no sistema:

    # - Estabelecer um limite de 10 transações diárias para uma conta
    # - Se o usuário tentar fazer uma transação após atingir o limite, deve ser informado que ele excedeu o número de transações permitidas para aquele dia
    # - Mostre no extrato, a data e hora detodas as transações

from datetime import datetime, timedelta

def retorna_ymd():
    data = datetime.strftime(datetime.now(), "%Y/%m/%d")
    return data
def retorna_hms():
    hora = datetime.strftime(datetime.now(), "%H:%M:%S")
    return hora

def verifica_limite_transacoes(extrato, data):
    # Verifica se esse dia já consta como chaveS
    if data in extrato.keys():
        dados_dia = extrato[data]
        if dados_dia['limite_transacao'] == 10:
            return False
        else:
            return True
    # Nao consta como chave, logo, não existe limite para este dia
    return True

def imprime_extrato_deposito(extrato):
    print(10*"=")
    print(10*"=")
    print('|Depósitos|')
    for key, value in extrato.items():
        if key == 'saldo':
            continue
        for d in value['deposito']:
            print(f"{key} {d['hora']} | + R$ {d['valor']:.2f}")

def imprime_extrato_saque(extrato):
    print(10*"=")
    print(10*"=")
    print('|Saques|')
    for key, value in extrato.items():
        if key == 'saldo':
            continue
        for d in value['saque']:
            print(f"{key} {d['hora']} | - R$ {d['valor']:.2f}")

extrato = {
    'saldo': 0.00,
}

estrutura_transacao_dia = {
    'deposito': [],
    'saque': [],
    'limite_transacao': 0,
}

estrutura_transacao_hora = {
    'hora': '',
    'valor': 0.00
}

while True:

    print("|=== Sistema Bancário ===|")
    print(f"Saldo disponível: {extrato['saldo']:.2f}")
    print("1 - Depósito \n2 - Saque \n3 - Extrato \n4 - Sair")
    opcao = int(input("Digite a opção desejada: "))
    data = retorna_ymd()
    estrutura_dia = estrutura_transacao_dia.copy()
    estrutura_hora = estrutura_transacao_hora.copy()

    if opcao == 1:
        # Verifica se o limite de transacoes diárias ja foram realizados
        if verifica_limite_transacoes(extrato, data):
            valor = float(input('Digite o valor do depósito: '))
            while valor <= 0.00:
                print('Valor inválido. Tente novamente.')
                valor = float(input('Digite o valor do depósito: '))
            hora = retorna_hms()
            estrutura_hora['hora'] = hora
            estrutura_hora['valor'] = valor
            if data in extrato.keys():
                extrato[data]['deposito'].append(estrutura_hora)
            else:
                estrutura_dia['deposito'].append(estrutura_hora)
                extrato[data] = estrutura_dia.copy()   
            extrato[data]['limite_transacao'] += 1
            extrato['saldo'] += valor
            print(f'Transação em {data} nro {extrato[data]['limite_transacao']}/10\nO depósito de R$ {valor:.2f} foi realizado com sucesso.\n')
        else:
            print(f"Não é possível realizar novos depósitos. Limite de transações diárias atingido para a data {data}.\n")
    elif opcao == 2:
        if verifica_limite_transacoes(extrato, data):
            valor = float(input('Digite o valor do saque: '))
            while valor <= 0.00 or valor > 500.00:
                print('Valor inválido. Digite um valor maior que zero e menor que 501.')
                valor = float(input('Digite o valor do saque: '))
            if valor > extrato['saldo']:
                print(f"Saldo {extrato['saldo']:.2f} insuficiente para o saque de {valor:.2f}\n")
            else:
                hora = retorna_hms()
                estrutura_hora['hora'] = hora
                estrutura_hora['valor'] = valor
                if data in extrato.keys():
                    extrato[data]['saque'].append(estrutura_hora)
                else:
                    estrutura_dia['deposito'].append(estrutura_hora)
                    extrato[data] = estrutura_dia
                extrato[data]['limite_transacao'] += 1
                extrato['saldo'] -= valor
                print(f"Transação em {data} nro {extrato[data]['limite_transacao']}/10\nO saque no valor de R$ {valor:.2f} foi realizado com sucesso.\n")
        else:
            print(f"Não é possível realizar novos saques. Limite de transações diárias atingido para a data {data}.\n")
    elif opcao == 3:
        print('---Extrato Bancário---')
        if len(extrato.keys()) == 1:
            print("Não houve transações.\n")
        else:
            imprime_extrato_deposito(extrato)
            imprime_extrato_saque(extrato)
            print(10*"=")
            print(10*"=")
        print(f"Saldo disponível: {extrato['saldo']:.2f}")
    elif opcao == 4:
        print("Encerrando o programa...\nPrograma encerrado.")
        break
    else:
        print("Digite uma opção válida.\n")
        