#EXEMPLO 5 - Fatorial de um número
'''
Crie um progama que recebe um número e imprime o seu fatorial

# Método 5Q's para montar um algorítimo:

Analise criticamente o problema e descubra:
(Tente explicar este problema para você mesmo em volz alta e peça mais informações/investigue mais até você mesmo compreender completamente o problema.)

1. Quais são os dados de entrada necessários?
2. O que devo fazer com estes dados?
3. Quais são as restrições deste problema?
- O número deve ser um valor positivo
- O número deve ser um valor inteiro
4. Qual o resultado esperado?
- O resultado esperado é que o fatorial do número seja providenciado seja exibido
5. Qual é sequência de passos a ser feita para chegar ao resultado esperado?
input numero
if numero > 0
if numero = inteiro
fatorial = 1
loop de 1 a numero:
  fatorial = fatorial * numero
print (fatorial)
'''
numero = int(input('Digite um número '))
if numero > 0:
  fatorial = 1
  for item in range (1,numero +1):
    fatorial = fatorial * item
  print(fatorial)