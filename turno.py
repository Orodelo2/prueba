import miscellaneous as mis
import random
import graficoCucaracha as g

def lanzar(jugador,tablero,puntos,penalidad,case,acumulado):
  dado = [1,2,3,4,5]
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
      mis.limpiar()
      print('='*25)
      print('PREMIO ACUMULADO: $' + str( acumulado))
      print('='*25)
      print('     >>>',jugador,'<<<')
      print('='*25)
      print('puntos:',puntosAux,end=' ')
      print('| Penalidad: $',penalidadAux)
      print('='*25)
      print('Resultado de los dados')
      for i in range(dados):
        random.shuffle(dado)
        listAux.append(dado[0])
        if dado[0] == 1:
          contador+=1
        print(dado[0],end='\t')

      if 1 in listAux: 
        #texto = '\nSiguiente lanzamiento, presione <enter>...'
        listAux= []
      else:
        texto = '\nFin de turno, presione <enter>...'
      
      #mis.next(texto)
      print()
      print('-'*25)

      #Se asigna la ganancia o se paga el case si pierde el turno por no sacar 1s
      if 0 < contador < 4:
        dados -= contador
        puntosAux = g.actualizarTablero(tablero,contador,puntosAux)
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
        if contador == 4:
          print('\nHaz sacado 4 números 1 en un solo lanzamiento, serás penalizado.')
          texto = '\nFin de turno, presione <enter>...'
        penalidadAux += case*0.1
        acumulado += penalidadAux
        cond = False
        mis.next(texto)
        print() 

    else:
      cond = False

  return puntosAux, penalidadAux, acumulado
