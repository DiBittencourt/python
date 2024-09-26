# Exercício 06
"""
No TP-2, Alice e Bob inventaram o seguinte método para codificar mensagens:
1) Dividem a mensagem ao meio
2) A primeira metade da mensagem vai ocupar as posições pares do texto. Já a segunda metade vai ocupar as posições ímpares. Considerando que a primeira posição é a 0.

Por exemplo, a mensagem "Olá Alice." seria transformada em:

        posicao |0 1 2 3 4 5 6 7 8 9 
           pares|O # l # á #   # A #    
        ímpares |# l # i # c # e # .
         ____________________________

mensagem_encriptada = Olliác eA.
(Veja no moddle uma figura com esse exemplo)

A sua tarefa agora é escrever o código para ENCRIPTAR a mensagem. A mensagem a ser encriptada está definida na variável mensagem_original. Seu código deve conter comentários.
"""

mensagem_original = "Olá Alice! Resolvi mudar nossa criptografia, acredito que nossa última mensagem foi interceptada. Mas agora com esse novo método ninguém vai conseguir ler nossas mensagens."

i = 0
tam = int(len(mensagem_original))
count1 = 0
count2 = 0

metade_tam = int(tam/2)
metade_msg1 = mensagem_original[:metade_tam]
metade_msg2 = mensagem_original[metade_tam:]
mensagem_encriptada = ""

while i <= tam -1:
  if i % 2 == 0:
    mensagem_encriptada += metade_msg1[count1]
    i += 1
    count1 += 1

  else:
    mensagem_encriptada += metade_msg2[count2]
    i += 1
    count2 += 1

print(metade_tam)
print(f'{metade_msg1}{metade_msg2}\n')
print(mensagem_encriptada)