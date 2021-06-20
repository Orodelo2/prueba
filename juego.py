import turno as t
import miscellaneous as mis
#import graficoCucaracha as g

def play(tableros,numjug):
  jugadores = []
  puntos = []
  penalidad = []
  case = int(input('Ingrese valor del case: $'))
  acumulado = case*2
  
  #1. Solicita los nombres de la cantidad de jugadores definidos por numjug (numero de jugadores)
  #2. Crea la lista de jugadores y crea listas paralelas para puntos y penalidades
  for i in range(numjug):
    jugadores.append(input('Ingrese nombre del jugador ' + str(i+1) + ' : '))
    puntos.append(0)
    penalidad.append(0)
  
  cond = True
  while cond:
    for i in range(len(jugadores)):
      mis.limpiar()
      puntos[i],penalidad[i],acumulado = t.lanzar(jugadores[i],tableros[i],puntos[i],penalidad[i],case,acumulado)
      #g.actualizarTablero(matriz,pos)
      mis.limpiar()
      if puntos[i] >= 33:
        cond = False
        print('Ganó el jugador ' + str(jugadores[i]))
        print('¡Eres el feliz GANADOR de $' + str(acumulado))
        mis.next('<enter>')
        break

  

