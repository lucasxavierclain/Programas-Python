km= int(input('Quanto quilometros foram percorridos com o carro ? '))
dias= int(input('Quantos dias o carro ficou alugado ? '))
pdias= dias*60
pkm=km*0.15
final=pkm+pdias
print('O valor para pagar referente aos dias é R${}\nO valor para pagar referente aos km é R${}\nO total a ser pago é R${}'.format(pdias,pkm,final))