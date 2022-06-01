"""
Um estudante de ensimo médio precisa escrever um pequeno programa 
interativo para calcular a superfície de um cilindro. Pede-se que 
você escreva o programa de acordo com sua especificação
"""

import math

print("Cálculo da Superfície de um Cilindro\n---")
diametro=float(input('Medida do diâmetro? '))
altura=float(input('Medida da altura? '))
area=2*(math.pi*(diametro/2)**2) + math.pi*diametro*altura
print('---\nÁrea calculada: %.2f' %area)

# math.pi equivale a 3.14
# para math.pi ser utilizado é necessario importar math
