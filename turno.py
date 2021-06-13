import miscellaneous as mis
import random
import graficoCucaracha as g

def lanzar(jugador,tablero,listPuntos):
  dado = [1,2,3,4,5,6,]
  listAux = []
  contador=0
  lanzamiento = 5
  cond = True
    
  print('='*15)
  print('Turno jugador',jugador)
  print('='*15)
  mis.next('Presione <enter> para lanzar')
  while cond:
    mis.limpiar()
    print('='*15)
    print('Turno jugador',jugador)
    print('='*15)
    print('puntos:',listPuntos[jugador-1])
    print('='*15)
    print('Resultado de los dados')
    for i in range(lanzamiento):
      random.shuffle(dado)
      listAux.append(dado[0])
      if dado[0] == 1:
        contador+=1
      print(dado[0],end='\t')

    if 1 in listAux: 
      texto = '\nSiguiente lanzamiento, presione <enter>...'
      listAux= []
    else:
      texto = '\nFin de turno, presione <enter>...'
     
    #mis.next(texto)
    print()
    print('-'*20)

    if contador > 0:
      lanzamiento -= contador
      listPuntos[jugador-1] = g.actualizarTablero(tablero,contador,listPuntos[jugador-1])
      contador = 0
    else:
      cond = False
    
    mis.next(texto)
    print()
