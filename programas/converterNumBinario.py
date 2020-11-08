
num=int(input('Digite um número '))
print('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL ''')
opção=int(input('Sua opção : '))
if opção==1:
    print('{} convertido em BINÁRIO é igual a {}'.format(num,bin(num)[2:])) #O '[2:]' significa que apartir do segundo digito que é mostrado
elif opção==2:
    print('{} convertido em OCTAL é igual a {}'.format(num,oct(num)[2:]))
elif opção==3:
    print('{} convertido em HEXADECIMAL é igual a {}'.format(num,hex(num)[2:]))
else:
    print('Digite uma opção válida')