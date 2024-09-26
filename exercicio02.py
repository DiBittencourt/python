# Exercício 02
"""
Crie uma lista com números que o usuário informar até que ele digite 'q'.
Exiba a soma dos números informados, a média e o desvio-padrão.
Não utilize bibliotecas ou funções para o cálculo da soma, média e desvio padrão.

Exemplo de execução:
Digite um número (q para sair): 5
Digite um número (q para sair): 10
Digite um número (q para sair): -3
Digite um número (q para sair): q
A soma dos números informados é: 12
A média dos números informados é: 4
O desvio-padrão dos números informados é: 6.5574

No moodle, é possível ver a fórmula para cálculo do desvio padrão.
Veja um exemplo em: https://pt.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/variance-standard-deviation-sample/a/population-and-sample-standard-deviation-review


"""
from math import sqrt

# Pede o primeiro numero para o usuario
num = input("Digite o primeiro numero. Para sair, digite q: \n")
# Cria lista para fazer o somatorio e declara as variaveis numericas dando valor 0
lista = []
soma = 0
somatorio = 0
n = 0
media = 0

# Repete enquanto num for diferente de q
while num.lower() != "q":
# Verifica se é digito positivo ou negativo
  if num.isdigit() or num[1:].isdigit():
# Incrementa a o contador
    n+=1
# Transforma em float
    num = float(num)
# Soma os valores
    soma += num
# Faz a media dos valores
    media = soma / n
# Adiciona em uma lista o numero
    lista.append(num)
    
    num = input("por gentileza, digite um novo numero ou q para sair: \n")
  else:
    num = input("por gentileza, digite um numero ou q pra sair: \n")

for i in lista:
  somatorio += (i - media)**2
  
desvio_padrao = round(sqrt(somatorio/(n -1)),4)

print(f"Soma dos numeros: {soma}\nMedia: {media}\nDesvio padrao: {desvio_padrao}\n Fim!")