import miscellaneous as mis

def crearTablero(tablero):
  
  f0  = [' ','X',' ',' ',' ','X',' ']
  f1  = [' ',' ','X',' ','X',' ',' ']
  f2  = [' ',' ',' ','X',' ',' ',' ']
  f3  = [' ',' ','x',' ','2',' ',' ']
  f4  = ['-','1','1',' ','1','1','-']
  f5  = ['|',' ','|',' ','|',' ','|']
  f6  = [' ',' ','|',' ','|',' ',' ']
  f7  = ['-','1','1',' ','1','1','-']
  f8  = ['|',' ','|',' ','|',' ','|']
  f9  = [' ',' ','|',' ','|',' ',' ']
  f10 = [' ','1','1',' ','1','1',' ']
  f11 = ['1',' ','|',' ','|',' ','1']
  f12 = ['|',' ','1',' ','1',' ','|']
  f13 = ['|',' ',' ','X',' ',' ','|']

  tablero.append(f0)
  tablero.append(f1)
  tablero.append(f2)
  tablero.append(f3)
  tablero.append(f4)
  tablero.append(f5)
  tablero.append(f6)
  tablero.append(f7)
  tablero.append(f8)
  tablero.append(f9)
  tablero.append(f10)
  tablero.append(f11)
  tablero.append(f12)
  tablero.append(f13)


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
  