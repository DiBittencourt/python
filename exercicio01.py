# Exercício 01
"""
Calcule a soma de todos os números pares de 1 a N, onde N é um número informado pelo usuário.

Exemplo de execução:
Digite um número: 10
A soma dos números pares de 1 a 10 é: 30
"""
# Solicita o numero indice de repetições no programa
n = int(input(" Digite um numero limite, para calcular a soma dos pares: \n"))
i = 0
soma = 0
# Repetir o laço ate que chegue no valor informado em n
while i < n:
# Incrementa o indice
  i = i+1
# Verifica o resto para ver se eh par
  if i % 2 == 0:
# Incrementa a soma
    soma += i
print (f"Num total de {i} numeros, a soma dos numeros pares eh: {soma}\n")