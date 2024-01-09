import classeConta

# Solicita o saldo inicial da pessoa.
saldoInicial = float(input('Informe o saldo inicial da conta: '))

# Cria um objeto Conta.
conta = classeConta.NovaConta(saldoInicial)
# Deposita o salário da pessoa.
salario = float(input('Quanto você recebeu de salário? '))
print('Seu salário está sendo depositado.')
conta.depositar(salario)

# Mostra o saldo.
saldoAtual = conta.verSaldo()
print(f'Seu saldo atual é: R$ {saldoAtual}')

# Perguntar saque.
valorSaque = float(input('Quanto deseja sacar? '))
print('O saque está sendo efetuado.')
conta.sacar(valorSaque)

# Mostrar saldo final
saldoAtual = conta.verSaldo()
print(f'Seu saldo atual é: R$ {saldoAtual}')