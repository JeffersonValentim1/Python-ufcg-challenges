"""
Faça um programa que calcule o delta de uma equação do segundo grau. 
Dados os coeficientes a, b e c, o delta é calculado elevando-se b 
ao quadrado e diminuindo desse valor a multiplicação de 4 por a e c.
"""

a=float(input())
b=float(input())
c=float(input())
delta = b*b - (4*a*c)
print('%.1f' % delta)
