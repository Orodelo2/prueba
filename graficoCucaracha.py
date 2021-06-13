import miscellaneous as mis

def crearTablero(tablero):
  
  f0  = [' ','2',' ',' ',' ','2',' ']
  f1  = [' ',' ','2',' ','2',' ',' ']
  f2  = [' ',' ',' ','2',' ',' ',' ']
  f3  = [' ',' ','2',' ','2',' ',' ']
  f4  = ['-','1','1',' ','1','1','-']
  f5  = ['|',' ','|',' ','|',' ','|']
  f6  = [' ',' ','|',' ','|',' ',' ']
  f7  = ['-','1','1',' ','1','1','-']
  f8  = ['|',' ','|',' ','|',' ','|']
  f9  = [' ',' ','|',' ','|',' ',' ']
  f10 = [' ','1','1',' ','1','1',' ']
  f11 = ['1',' ','|',' ','|',' ','1']
  f12 = ['|',' ','1',' ','1',' ','|']
  f13 = ['|',' ',' ','3',' ',' ','|']

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

  #for i in range(len(matriz)):
  #  for j in range(len(f0)):
  #    print(matriz[i][j],end='\t')
  #  print()

  #mis.next('<enter>')


def actualizarTablero(matriz,pos,points):
  pos2 = str(pos)
  salto = False
  puntos = points
  #cond = True
  #while cond:
  #mis.limpiar()
  #pos = input('ingrese pos >>> ')
  salto = False
  for i in range(len(matriz)):
    for j in range(7):
      #print(i)
      #print(j)
      #print(matriz[i][j])
      if pos2 in matriz[i][j]:
        matriz[i][j] = 'X'
        salto = True
        puntos += pos
        break
    if salto == True:
      break

  for i in range(len(matriz)):
    for j in range(7):
      print(matriz[i][j],end='\t')
    print()
  
  return puntos
  #mis.next('<enter>')