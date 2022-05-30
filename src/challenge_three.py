'''
Pintor

Escreva um programa que ajude um pintor de paredes a calcular o custo de seu serviço. 
Ele cobra o valor de R$ 20,00 por metro quadrado de área pintada. O programa deve 
ler da entrada as dimensões de uma parede retangular (altura, largura) e deve calcular 
e imprimir o custo em reais do serviço. Assuma que todas as paredes são retangulares e que os 
espaços de portas, janelas ou outros obstáculos nas paredes não são considerados para fins de desconto.

'''

altura = float(input())
largura = float(input())
area = altura * largura
valor = area * 20.00
print('%.2f' % valor)
