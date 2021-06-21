import miscellaneous as mis
import pickle

def numeroJugadores():
  cond = True
  while cond:
    try:  
      mis.limpiar()
      print('='*30)
      print('     JUEGO LA CUCARACHA')
      print('='*30)
      numJugadores = int(input('Ingrese número de jugadores\n>>> '))
      if 1 < numJugadores <= 7:
        cond = False
      else:
        mis.limpiar()
        print('='*30)
        print('     JUEGO LA CUCARACHA')
        print('='*30)
        print('Ingrese cantidad de jugadores entre 2 y 7')
        mis.next('<enter>')
    except:
      mis.limpiar()
      print('='*30)
      print('     JUEGO LA CUCARACHA')
      print('='*30)
      print('\nIngrese cantidad de jugadores entre 2 y 7')
      mis.next('<enter>')
  
  return numJugadores

def revisar(texto):
  cond = True
  while cond:
    try:  
      mis.limpiar()
      print('='*30)
      print('     JUEGO LA CUCARACHA')
      print('='*30)
      var = int(input(texto))
      cond = False
    except:
      mis.limpiar()
      print('='*30)
      print('     JUEGO LA CUCARACHA')
      print('='*30)
      print('Ingrese cantidad valida')
      mis.next('<enter>')
  
  return var

def validar(texto):
  
  S_N = input(texto)
  S_N = S_N.casefold()  #se elimina el case sensitive
  if S_N == 's' or S_N == 'si':
    w = True
    flag = False
  elif S_N == 'n' or S_N == 'no' :
    w = False
    flag = False
  else:
    input('Ingrese opción valida...<enter> ')
    w = None
    flag = True

  
  return w, flag

def cargarJugadores():
  try:
    archivo = open("jugadores.dat","rb")
    jugadores = pickle.load(archivo)
    archivo.close()
  except:
    archivo = open("jugadores.dat","wb")
    pickle.dump(jugadores,archivo)
    archivo.close()
  
  return jugadores

def crear(jugadores):
  try:
    archivo = open("jugadores.dat","wb")
    pickle.dump(jugadores,archivo)
    archivo.close()
  except:
    None
