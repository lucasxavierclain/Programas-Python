import random
import time
a1='PEDRA'
a2='PAPEL'
a3='TESOURA'
jogo=[a1,a2,a3]
print('Vamos começar o Jokenpô\nDigite a sua escolha ')
escolha=str(input('Pedra, papel ou tesoura ?')).upper()
random.shuffle(jogo)
aleatorio=jogo[0]
time.sleep(1)
print('A máquina escolheu ',aleatorio.title())

if(jogo[0]==escolha):
    print('Deu empate')
elif (escolha=='PEDRA' and jogo[0]=='PAPEL' or escolha=='PAPEL' and jogo[0]=='TESOURA' or escolha=='TESOURA' and jogo[0]=='PEDRA' ):
    print('Você perdeu, {} ganha de {}'.format(escolha.title(), jogo[0].title()))
elif(escolha=='PAPEL' and jogo[0]=='PEDRA' or escolha=='PEDRA' and jogo[0]=='TESOURA' or escolha=='TESOURA' and jogo[0]=='PAPEL'):
    print('Você ganhou, {} ganha de {}'.format(escolha.title(),jogo[0].title()))
else:
    print('Escolha um item válido')