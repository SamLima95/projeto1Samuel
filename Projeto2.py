# Projeto - Chute o número
'''
Escreva um programa que, ao iniciar gera um valor aleatório de 1 a 10 e permite que o usuário chute um número até que o valor aleatório gerado no início do programa seja chutado corretamente.

O programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatório gerado no inico do programa

# Metodo 5Q's para montar um algorítimo

Analise criticamente o problema e descubra:
(Tente explicar este problema para você mesmo em voz alta e peça mais infromações/investigue mais até você compreender o problema.)

1. Quais são os dados de entrada necessários?
- Valor aleatório de 1 a 10
- Chute do usuário
2. O que devo fazer com estes dados?
- Eu devo comparar o chute do usuário com o valor aleatório que foi gerado no início do programa e dizer se foi maior, menor ou igual ao valor que foi ferado no inicio do progama
3. Quais são as restrições deste problema?
- Um valor aleatório de 1 a 10
4. Qual o resultado esperado?
- O resultado esperado é programa deve informar se o chute do usuário com o valor aleatório que foi gerado no início do programa e dizer se foi maior, menor ou igual ao valor que foi ferado no inicio do progama
5. Qual é sequência de passos a ser feita para chegar ao resultado esperado?
input valor_aleatorio de 1 a 10
input chute
if chute > valor_aleatorio:
Print "Chute foi mair que o valor gerado"
if Chut < valor_aleatorio
Print "Chute foi menor que o valor gerado"
if Chute == valor_aleatorio
print "Voce acertou"
'''
import random

valor_aleatorio = random.randint(1,10)
acertou = False
while acertou == False:
  chute = int(input ('Chute um valor de 1 a 10> '))
  if chute > valor_aleatorio:
    print('Chute foi mair que o valor gerado')
  elif chute < valor_aleatorio:
    print('Chute foi menor que o valor gerado')
  elif chute == valor_aleatorio:
    acertou = True
    print('Você acertou! Parabéns')
    