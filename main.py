import graficoCucaracha as g
import juego
import miscellaneous as mis

tableros = [] #Definimos Lista para guardar todos los tableros
matriz  = [] #Defino tablero jugador 1
matriz2 = [] #Defino tablero jugador 2
matriz3 = [] #Defino tablero jugador 3
matriz4 = [] #Defino tablero jugador 4
matriz5 = [] #Defino tablero jugador 5
matriz6 = [] #Defino tablero jugador 6
matriz7 = [] #Defino tablero jugador 7

g.crearTablero(matriz) #Creamos el tablero del jugador 1
g.crearTablero(matriz2)#Creamos el tablero del jugador 2
g.crearTablero(matriz3)#Creamos el tablero del jugador 3
g.crearTablero(matriz4)#Creamos el tablero del jugador 4
g.crearTablero(matriz5)#Creamos el tablero del jugador 5
g.crearTablero(matriz6)#Creamos el tablero del jugador 6
g.crearTablero(matriz7)#Creamos el tablero del jugador 7

#Creamos la lista de tableros, para guardar todos los tableros de los jugadores
tableros.append(matriz)
tableros.append(matriz2)
tableros.append(matriz3)
tableros.append(matriz4)
tableros.append(matriz5)
tableros.append(matriz6)
tableros.append(matriz7)

#Validar que el número de jugadores sea entre 2 y 7.
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
cond = mis.againEscapeNega(input('Desea jugar nuevamente, S/N >>> '))