'''
Projeto - Medidor de velocidade

Levando em consideração a velicidade máxima permitida de 80km em uma determinada rua. Crie um programa que recebe do usuário um valor que representa a velocdade e com base nessa velocidade diga se ela tomou uma multa leve. grave ou gravissíma. Levando em consideração que se a pessoia estiver abaixo da velocidade máxima seu programa deve exibir "não houve multa", caso esteja até 10 km acima deve exibir: "Levou multa levee" e caso esteja entre 11 a 20 km acima da velocidade máxima exibir: "Levou multa grave", e caso esteja acima de 20km acima da velocidade máxima, exibir: "Levou multa gravissima"

Analise criticamente o problema e descubra:
(Tente explicar este problema para você mesmo em voz alta e peça mais informações/investigue mais até voce compreender completamente o problema.)

1. Quais são os dados de entrada necessários?
- Velocidade
2. O que devo fazer com estes dados?
- Levando em consideração que se a pessoia estiver abaixo da velocidade máxima seu programa deve exibir "não houve multa", caso esteja até 10 km acima deve exibir: "Levou multa levee" e caso esteja entre 11 a 20 km acima da velocidade máxima exibir: "Levou multa grave", e caso esteja acima de 20km acima da velocidade máxima, exibir: "Levou multa gravissima"
3. Quais são as restrições deste problema

4. Qual é o resultado esperado?
- O resultado esperado é exibir a mensagem que corresponde ao nível da multa que a pessoa levou (deve exibir "não houve multa", caso esteja até 10 km acima deve exibir: "Levou multa levee" e caso esteja entre 11 a 20 km acima da velocidade máxima exibir: "Levou multa grave", e caso esteja acima de 20km acima da velocidade máxima, exibir: "Levou multa gravissima")
5. Qual é sequência de passos a ser feitas para chegar ao resultado esperado?
input valocidade
velocidade_maxima = 80
if velocidade <= velocidade_maxima:
  Print(Não levou multa)
if velocidade > velicidade_maxima e velocidade <= velocidade_maxiam + 10:
  print('Você levou multa leve')
if velocidade > velocidade_maxma +11 e velocidade <= velicudade_maxima +20:
  print (Levou multa grave)
if velocidade > velicidade_maxima +20:
  print "Levou multa gravissima"

'''
velocidade = int(input('Digite sua velocidade: '))
velocidade_maxima = 80
if velocidade <= velocidade_maxima:
  print('Não levou multa')
elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima + 10:
  print('Levou multa leve')
elif velocidade >= velocidade_maxima + 11 and velocidade <= velocidade_maxima + 20:
  print ('Levou multa grave')
elif velocidade > velocidade_maxima + 20:
  print('Levou multa gravíssima')