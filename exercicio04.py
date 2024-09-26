# Exercício 04
"""
Escreva um código que peça um número para o usuário e responda se ele é primo ou não.
Lembrando que um número primo é um número maior que 1 que só pode ser dividido por 1 e por ele mesmo.
Seu código deve conter comentários.
"""
# Solicita numero
num = int(input("Digite um numero para saber se ele eh primo ou nao:\n"))
primo = 0
# Faz a repeticao ate o numero indicado
for i in range(num):
#verifica se o numero eh divisivel, o indice maior que 0 e diferente dele mesmo
  if num % (i+1) == 0 and i > 0 and num != i +1:
    primo += 1
# Mostra se nao teve repeticao, eh promo
if primo == 0:
    print("O numero eh primo!")
else:
    print("O numero nao eh primo!")