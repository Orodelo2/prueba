import miscellaneous as mis
import random
import graficoCucaracha as g

def encabezado(acumulado,jugador,puntosAux,penalidadAux,listAux):
  mis.limpiar()
  print('='*25)
  print('PREMIO ACUMULADO: $' + str(acumulado))
  print('='*25)
  print('     >>>',jugador,'<<<')
  print('='*25)
  print('puntos:',puntosAux,end=' ')
  print('| Penalidad: $',penalidadAux)
  print('='*25)
  print('Resultado de los dados')
  for i in range(len(listAux)):
    print(listAux[i],end='\t')
  print()
  print('-'*25)

def printTablero(tablero):
  for i in range(len(tablero)):
    for j in range(7):
      print(tablero[i][j],end='\t')
  print()

def lanzar(jugador,tablero,puntos,penalidad,case,acumulado):
  dado = [1,1,1,4,5]
  listAux = []
  contador=0
  dados = 5
  cond = True
  puntosAux = puntos
  penalidadAux = penalidad
      
  print('='*25)
  print('Turno jugador:',jugador)
  print('='*25)
  mis.next('Presione <enter> para lanzar')
  
  while cond:
    #controla 
    #1. si un jugador gana al tener 33 puntos.
    #2. Si cede el turno al no sacar 1s.
    #3. si el jugador debe pagar o recibir ganancia.
    if puntosAux < 33:
      listAux= []  

      for i in range(dados):
        random.shuffle(dado)
        listAux.append(dado[0])
        if dado[0] == 1:
          contador+=1

      print()
      print('-'*25)

      #Se asigna la ganancia o se paga el case si pierde el turno por no sacar 1s
      if 0 < contador < 4:
        dados -= contador
        # 0   1   2   3
        #[0, C1, C2, C3]
        puntosAux = g.actualizarTablero(tablero,contador,puntosAux)
        encabezado(acumulado,jugador,puntosAux,penalidadAux,listAux)

        for i in range(len(tablero)):
          for j in range(7):
            print(tablero[i][j],end='\t')
          print()
        #gananciaAux += case
        contador = 0

        #reinicia a 5 dados si el número de dados es cero por sacar 1s repetidamente en los lanzamientos.
        if dados != 0:
          #pregunta si el jugador desea lanzar nuevamente
          cond = mis.againEscapeNega(input('Desea lanzar nuevamente, S/N >>> '))
        else:
          cond = False
      elif contador == 5:
        puntosAux = 33
        print('\nFelicidades, has sacado puntaje perfecto en un lanzamiento, ¡haz ganado!')
        mis.next('Presione <enter> para continuar')
      else:
        penalidadAux += case*0.1
        acumulado += penalidadAux

        encabezado(acumulado,jugador,puntosAux,penalidadAux,listAux)

        if contador == 4:
          print('\nHaz sacado 4 números 1 en un solo lanzamiento, serás penalizado.')
        
        cond = False
        mis.next('\nFin de turno, presione <enter>...')
        print() 

    else:
      cond = False

  return puntosAux, penalidadAux, acumulado
