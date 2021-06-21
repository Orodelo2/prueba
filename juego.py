import turno as t
import miscellaneous as mis
import validaciones as val
#import graficoCucaracha as g

def play(tableros,numjug,condicion):
  mis.titulo()
  case = val.revisar('Ingrese valor del case: $')
  multa = val.revisar('Ingrese valor de la multa: $')
  acumulado = case*2
  
  mis.titulo()
  
  #1. Solicita los nombres de la cantidad de jugadores definidos por numjug (numero de jugadores)
  #2. Crea la lista de jugadores y crea listas paralelas para puntos y penalidades
  if condicion == True:
    jugadores = []
    puntos = []
    penalidad = []
    for i in range(numjug):
      print('Ingrese nombre del jugador ' + str(i+1) + ' :')
      nombre = input('>>> ')
      jugadores.append(nombre.upper())
      puntos.append(0)
      penalidad.append(0)
    val.crear(jugadores)
  else:
    jugadores = val.cargarJugadores()
    puntos = []
    penalidad = []
    for i in range(numjug):
      puntos.append(0)
      penalidad.append(0)
  
  cond = True
  while cond:
    for i in range(len(jugadores)):
      mis.limpiar()
      puntos[i],penalidad[i],acumulado = t.lanzar(jugadores[i],tableros[i],puntos[i],penalidad[i],case,acumulado,multa)
      #g.actualizarTablero(matriz,pos)
      mis.limpiar()
      if puntos[i] >= 33:
        cond = False
        print('Ganó el jugador ' + str(jugadores[i]))
        print('¡Eres el feliz GANADOR de $' + str(acumulado))
        mis.next('<enter>')
        break

  

