forma=str(input('Qual a forma de pagamento? Dinheiro, cartão ou cheque? ')).upper().split()
valor=float(input('Digite o valor do produto que você quer comprar '))

if('CARTÃO' in forma):
    parcela=int(input('Digite o número de parcelas '))
    if(parcela==1):
        desconto= valor-(valor*5/100)
        print('O valor com desconto fica R$ ',desconto)
    elif(parcela==2):
        print('Ficará em 2x de R${:.2f}'.format(valor/2))
    else:
        juros=valor+(valor*20/100)
        print('Ficará em {}x de R${:.2f}'.format(parcela,juros/parcela))
        
elif ('DINHEIRO' or 'CHEQUE' in forma):
    vf=valor-(valor*10/100)
    print('O valor com desconto fica R$', vf)
else: 
    print('Digite uma das formas válidas ')