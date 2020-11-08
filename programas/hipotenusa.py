import math
opsto=int(input('Digite o cateto oposto '))
adj=int(input('Digite o cateto adjascente '))

hip=math.hypot(opsto,adj)
print('A hipotenusa é {:.2f}'.format(hip))