import graficoCucaracha as g
import juego
import miscellaneous as mis

tableros = []
matriz  = []
matriz2 = []
matriz3 = []
matriz4 = []
matriz5 = []
matriz6 = []
matriz7 = []

g.crearTablero(matriz)
g.crearTablero(matriz2)
g.crearTablero(matriz3)
g.crearTablero(matriz4)
g.crearTablero(matriz5)
g.crearTablero(matriz6)
g.crearTablero(matriz7)

tableros.append(matriz)
tableros.append(matriz2)
tableros.append(matriz3)
tableros.append(matriz4)
tableros.append(matriz5)
tableros.append(matriz6)
tableros.append(matriz7)

cond = True

while cond:
  try:  
    mis.limpiar()
    numJugadores = int(input('Ingrese número de jugadores >>> '))
    if 1 < numJugadores <= 7:
      cond = False
    else:
      print('Ingrese cantidad de jugadores entre 2 y 7')
      mis.next('<enter>')
  except:
    mis.limpiar()
    print('Ingrese cantidad de jugadores entre 2 y 7')
    mis.next('<enter>')



juego.play(tableros,numJugadores)