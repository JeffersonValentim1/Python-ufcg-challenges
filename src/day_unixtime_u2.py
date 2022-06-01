"""
Em alguns programas de computador, é comum referenciar a hora atual de um sistema através do chamado "Unix time" ou "POSIX time". 
Este valor é calculado pelo número de segundos que se passaram desde a hora zero do dia 1º de Janeiro de 1970. 
Crie um programa calcula esse número de dias.
"""

day_one=int(input())
days= day_one//86400
print(days)
