
def cargarTablero():
  global tablerotxt
  hand = open('tablero.txt','r')
  tablerotxt = hand.read()
  hand.close()

def crearTablero():  
  tablero = []
  listaAux = []
  for line in tablerotxt:
    if not line.startswith("\n"):
      listaAux.append(line)
    else:
      tablero.append(listaAux)
      listaAux = []
  
  return tablero
  

def actualizarTablero(matriz,pos,points):
  pos2 = str(pos)
  salto = False
  puntos = points
  cond = True

  #actualizar la cucaracha
  #buscando el número 1, 2 o 3 en la matriz cucaracha para reemplazarlo
  while cond:
    for i in range(14):
      for j in range(7):
        if pos2 in matriz[i][j]:
          matriz[i][j] = 'X'
          salto = True
          puntos += pos
          break
      if salto == True:
        break
  
  #resta una unidad al resultado de los dados cuando no hay valores disponibles en la cucaracha para llenar con dicho reultado, y llenar una casilla con un valor inferior. ejemplo, resultao = 3, y no hay 3 disponible en el tablero, entonces resta 1 y busca llenar un 2 en el tablero, si no hay 2 resta 1 y busca llenar un 1.
  
    if pos > 1 and salto == False:
      pos -= 1
      pos2 = str(pos)
    else:
      cond = False

  return puntos
  