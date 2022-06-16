"""
Calcula ingressos do cinema

João e Maria pretendem levar amigos e filhos ao cinema. Escreva um programa que leia o número de adultos, o número de crianças e o preço do ingresso do cinema e imprima o valor total a ser pago. Considere que todas as crianças pagam meia entrada.
Entrada

A entrada consiste em três linhas. Na primeira, se registra o número de adultos; na segunda, o número de crianças; e na terceira, o preço do ingresso do cinema. Abaixo, um exemplo de entrada.

2
3
12

Saída

A saída deve ter uma única linha contendo o valor total a ser pago, expresso com duas casas decimais. O exemplo abaixo demonstra a formatação esperada. Essa saída corresponde à entrada acima.

Total: R$ 42.00

"""

na= int(input())
nc= int(input())
pr=float(input())
indult=int(na*pr)
prcri=(int(pr)/2) * nc
resultado= indult + prcri
print(f'Total: R$ {resultado:.2f}')
