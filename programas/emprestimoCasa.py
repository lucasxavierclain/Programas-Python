import time
print('Para solicitar os dados para empréstimo digite os dados abaixo...')
time.sleep(1)
casa=float(input('Qual o valor da casa? '))
salario=float(input('Qual o seu salário? '))
anos=float(input('Quantos meses você pretende pagar? '))

if(salario<0 or casa<0):
    print('Valores inválidos')
elif(casa/anos>salario*30/100):
    print('Seu empréstimo foi negado ')
elif(casa/anos<salario*30/100):
    print('Seu emprestimo foi aceito')
    print('A parcela será de R${:.2f} em {:.0f} meses'.format(casa/anos,anos))

