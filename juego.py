import turno as t
import miscellaneous as mis
#import graficoCucaracha as g

def play(tableros,numjug):
  jugadores = []
  puntos = []
  for i in range(numjug):
    jugadores.append(i+1)
    puntos.append(0)
  #pos = 0
  cond = True
  while cond:
    for i in range(len(jugadores)):
      mis.limpiar()
      t.lanzar(jugadores[i],tableros[i],puntos)
      #g.actualizarTablero(matriz,pos)
      mis.limpiar()

    
