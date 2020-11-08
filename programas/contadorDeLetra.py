
frase=str(input('Digite uma frase ')).upper().strip()
letra=str(input('Digite a letra a ser pesquisada ')).upper()
contador=frase.count(letra)
if(len(letra)>1):
    print('Tem mais de uma letra')

else:
    print(f'A letra {letra} aparece {contador} vezes')
    print(f'A posição que ela aparece pela primeira vez é {format(frase.find(letra)+1)}')
    print(f'A posição que ela aparece pela última vez é {format(frase.rfind(letra)+1)}')
