# Exercício 03
"""
Escreva um programa que recebe uma lista de números inteiros do usuário.
O programa deve criar uma nova lista contendo apenas os números pares da lista original e imprimi-la.

Exemplo de execução:
Entre com os números separados por espaço: 1 2 3 4 5 6
Números pares: [2, 4, 6]
"""
num = input("Digite uma lista de numeros separado por espaços:\n").replace(" ","")
tam = len(num)
list = []
soma_par = 0
for i in range(tam):
  if int(num[i]) % 2 == 0:
    list.append(int(num[i]))

print(f'Os numeros pares são: {list}\n')