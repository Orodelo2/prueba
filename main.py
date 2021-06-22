import graficoCucaracha as g
import juego
import miscellaneous as mis
import presentacion as pre
import validaciones as val

#Definimos Lista para guardar todos los tableros
tableros = [] 
#carga el tablero des un txt para ser usado en el juego
g.cargarTablero()
#Creamos la lista de tableros, para guardar todos los tableros de los jugadores
for i in range(7):
  tableros.append(g.crearTablero())

def juegoNuevo(T):
  #Validar que el número de jugadores sea entre 2 y 7.
  global numJugadores 
  numJugadores = val.numeroJugadores()
  juego.play(tableros,numJugadores,T)

def againPlay(F):
  mis.limpiar()
  juego.play(tableros,numJugadores,F)

def continuar():
  global cond
  while True:
    mis.titulo()
    cond, flag = val.validar('Desea jugar nuevamente, S/N >>> ')
    if flag == False:
      break
    else:
      None


mis.limpiar()
pre.presentacion()

while True:
  opcion = mis.menu()

  if opcion == '1':
    mis.instrucciones()
    mis.next('<enter>, para volver...')
  elif opcion == '2':
    #ejecuta el juego por primera vez cuando se corre el juego
    mis.titulo()
    juegoNuevo(True)
    continuar()

    #controla la repetición del juego
    while True:
      if cond == True:
        opcion = input('Juego con Nuevos Jugadores, S/N: ')
        opcion = opcion.casefold()

        if opcion == 's' or opcion == 'si':
          juegoNuevo(True)
          continuar()
        else:
          againPlay(False)
          continuar()

      else:
        mis.titulo()
        print('\nJUEGO FINALIZADO')
        input('\nPresione <enter> para salir')
        mis.limpiar()
        break
  elif opcion == '3':
    mis.next('Juego Finalizado, <enter> ')
    break 
  else:
    mis.next('Ingrese opción válida, <enter> ')
