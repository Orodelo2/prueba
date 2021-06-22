import miscellaneous as mis
import random
import graficoCucaracha as g

def encabezado(acumulado,jugador,puntosAux,penalidadAux,listAux):
  mis.titulo()
  texto = '>>>'+jugador+'<<<'
  print('='*30)
  print('PREMIO ACUMULADO: $' + str(acumulado))
  print('='*30)
  print(texto.center(30))
  print('='*30)
  print('Puntos:',puntosAux)
  print('Penalidad: $',penalidadAux)
  print('='*30)

def verDados(listAux):
  print('Resultado de los dados')
  print('-'*30)
  for i in range(len(listAux)):
    print(listAux[i],end='\t')
  print()
  print('-'*30)

def printTablero(tablero):
  for i in range(14):
    for j in range(7):
      print(tablero[i][j],end='\t')
    print()

def lanzar(jugador,tablero,puntos,penalidad,case,acumulado,multa):
  dado = [1,2,3,4,5]
  listAux = []
  contadorUnos = 0
  dados = 5
  cond = True
  puntosAux = puntos
  penalidadAux = penalidad
  
  mis.titulo()
  print('Turno jugador:',jugador)
  print('='*30)
  mis.next('<enter> para iniciar el turno')
  
  while cond:
    #controla 
    #1. si un jugador gana al tener 33 puntos.
    #2. Si cede el turno al no sacar 1s.
    #3. si el jugador debe pagar o recibir ganancia.
    if puntosAux < 33:
      listAux= []  #Alamacena el valor de los 5 dados lanzados

      #Ejecuta los 5 lanzamientos de los dados
      for i in range(dados):
        random.shuffle(dado)
        listAux.append(dado[3])

      contadorUnos = listAux.count(1)

      #Se asigna la ganancia o se paga el case si pierde el turno por no sacar 1s
      if 0 < contadorUnos < 4:
        #resta un dado por cada 1 obtenido
        dados -= contadorUnos

        #imprime el encabezado de los datos del turno
        encabezado(acumulado,jugador,puntosAux,penalidadAux,listAux)
        mis.next('<enter> para lanzar') #pausa
        
        #envia el resultado de los dados para actualizar el tablero y totalizar los puntos obtenidos
        puntosAux = g.actualizarTablero(tablero,contadorUnos,puntosAux)

        encabezado(acumulado,jugador,puntosAux,penalidadAux,listAux)
        verDados(listAux)
        mis.next('<enter> para llenar tablero')

        encabezado(acumulado,jugador,puntosAux,penalidadAux,listAux)
        verDados(listAux)
        printTablero(tablero)

        contadorUnos = 0

        #reinicia a 5 dados si el número de dados es cero por sacar 1s repetidamente en los lanzamientos.
        if dados != 0:
          #pregunta si el jugador desea lanzar nuevamente
          cond = mis.againEscapeNega(input('\nDesea lanzar nuevamente, S/N >>> '))
        else:
          cond = False

      elif contadorUnos == 5:
        puntosAux = 33
        print('\nFelicidades, has sacado puntaje perfecto en un lanzamiento, ¡haz ganado!')
        mis.next('Presione <enter> para continuar')
      else:

        encabezado(acumulado,jugador,puntosAux,penalidadAux,listAux)
        mis.next('<enter> para lanzar')
        penalidadAux += multa
        acumulado += penalidadAux
        puntosAux = g.actualizarTablero(tablero,contadorUnos,puntosAux)
        encabezado(acumulado,jugador,puntosAux,penalidadAux,listAux)
        verDados(listAux)
        print('Pagas multa'.center(30))
        print('.'*30)
        mis.next('<enter> para ver tablero')
        encabezado(acumulado,jugador,puntosAux,penalidadAux,listAux)
        verDados(listAux)
        print('Pagas multa'.center(30))
        print('.'*30)
        printTablero(tablero)

        if contadorUnos == 4:
          print('\nHaz sacado 4 números 1 en un solo lanzamiento, serás penalizado.')
        
        cond = False
        mis.next('\nFin de turno, presione <enter>...')
        print() 

    else:
      cond = False

  return puntosAux, penalidadAux, acumulado
