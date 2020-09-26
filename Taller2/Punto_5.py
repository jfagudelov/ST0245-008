import random as rd

votos = []
votantes = rd.randint(101, 1001)
for i in range(1,votantes):
  votos.append(rd.randint(1,2))

def ganador_presidencia(lista_votos):
  votos_a = lista_votos.count(1)
  votos_b = lista_votos.count(2)
  mensaje_ganador_a = 'El ganador es el candidato 1 con {} votos'.format(votos_a)
  mensaje_ganador_b = 'El ganador es el candidato 2 con {} votos'.format(votos_b)
  return mensaje_ganador_a if votos_a > votos_b else mensaje_ganador_b

print(ganador_presidencia(votos))
