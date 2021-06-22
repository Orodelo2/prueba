import os

def instrucciones():
  limpiar()
  try:
    handler = open("Instrucciones.txt","r")
    instrucciones = handler.read()
    handler.close()
  except:
    None
  
  print(instrucciones)


#Función para generar una pausa por medio de un input de pantalla
def titulo():
  limpiar()
  print('='*30)
  print('JUEGO LA CUCARACHA'.center(30))
  print('='*30)

def next(texto):
  input('\n'+texto)

def again():
  S_N = input('\n¿Desea intentar nuevamente? S/N...')
  S_N = S_N.casefold()  #se elimina el case sensitive

  if S_N == 's' or S_N == 'si':
    w = True
  elif S_N == 'n' or S_N == 'no' :
    w = False
  
  return w

def againEscapeAfir(S_N):
  S_N = S_N.casefold()  #se elimina el case sensitive

  if S_N == 's' or S_N == 'si':
    w = False
  elif S_N == 'n' or S_N == 'no' :
    w = True
 
  return w

def againEscapeNega(S_N):
  S_N = S_N.casefold()  #se elimina el case sensitive

  if S_N == 's' or S_N == 'si':
    w = True
  elif S_N == 'n' or S_N == 'no' :
    w = False
  else:
    w = True
 
  return w
  
#Función para generar mensaje para selección de menu u opciones
def seleccionar():
  seleccion = input('\nDigite la opción a revisar...')
  return seleccion

#Función para establecer unidades de medidad de longitud
def msjUnidadMedida():
  texto = """
  Seleccione la unidad de medida de longitud a usar:
  1. cm
  2. m
  3. Km
  """
  print(texto)
  u = input('')
  if u == '1':
    uM = 'cm'
  elif u == '2':
    uM = 'm'
  else:
    uM = 'Km'
  return uM

#Función para establecer unidades de medidad de tiempo
def msjUnidadMedidaTiempo():
  texto = """
  Seleccione la unidad de medida de tiempo a usar:
  1. seg
  2. min
  3. Hrs
  """
  print(texto)
  u = input('')
  if u == '1':
    uM = 's'
  elif u == '2':
    uM = 'min'
  else:
    uM = 'h'
  return uM

#Función para borrar pantalla
def limpiar():
  if os.name == "posix":
    os.system ("clear")
  else:
    if((os.name == "ce") or (os.name == "nt") or (os.name == "dos")):
      os.system ("cls")

def funcion(a):
  a[0] = 10

def menu():
  titulo()
  print(' '*6,'1. Instrucciones')
  print(' '*6,'2. Jugar')
  print(' '*6,'3. Salir')
  print('-'*30)
  opcion = input('\nIngrese opción>>> ')
  
  return opcion
  