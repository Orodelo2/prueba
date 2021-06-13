
#    C C C
#    0 1 2
#F0 [1,2,3]
#F1 [4,5,6]
#F2 [7,8,9]
matriz=[[1,2,3],[4,5,6],[7,8,9]]
print(matriz)
print(matriz[0][0])
print(matriz[0][1])
print(matriz[0][2])
print(matriz[1][0])
print(matriz[1][1])
print(matriz[1][2])
print(matriz[2][0])
print(matriz[2][1])
print(matriz[2][2])

print("="*20)
for f in range(len(matriz)):
  for c in range(len(matriz)):
    print(matriz[f][c])
  print()

print("="*20)
for f in range(len(matriz)):
  for c in range(len(matriz)):
    print(matriz[f][c]," ",end="\t")
  print()
print("="*20)
#=======================================
f1=[1,"A",5]
f2=[5,"S",1]
f3=["A","A","S"]
matriz=[f1,f2,f3]
print(matriz)
print(matriz[1][2])

for f in range (len(matriz)):
  for c in range(len(matriz)):
    print(matriz[f][c],end="\t")
  print()

#==============================

f1=[1,2,3]
f2=[4,5,6]
f3=[7,8,9]
matriz=[f1,f2,f3]

for f in range(len(matriz)):
  for c in range (len(matriz)):
    if((matriz[f][c]%2)!=0):
      print(matriz[f][c]," Es Impar")

#====================================

f1=["A","B","C"]
f2=["D","I","F"]
f3=["G","H","I"]
matriz=[f1,f2,f3]

letra=input("Letra a Buscar : ")

for f in range(len(matriz)):
  for c in range (len(matriz)):
    if(matriz[f][c]==letra):
      print(matriz[f][c]," esta en la coordenada, ", f,c)
#=====================================

f1=[]
f2=[]
f3=[]
f4=[]
matriz=[]

#LLenar listas
for i in range(4):
  num=int(input("Valor : "))
  f1.append(num)

for i in range(4):
  num=int(input("Valor : "))
  f2.append(num)

for i in range(4):
  num=int(input("Valor : "))
  f3.append(num)

for i in range(4):
  num=int(input("Valor : "))
  f4.append(num)

matriz.append(f1)
matriz.append(f2)
matriz.append(f3)
matriz.append(f4)

for f in range (len(matriz)):
  for c in range(len(matriz)):
    print(matriz[f][c],end="\t")
  print()
  
suma_izq=0
for f in range (len(matriz)):
  for c in range(len(matriz)):
    if(f==c):
      suma_izq=suma_izq+matriz[f][c]
print("La suma es: ",suma_izq)

suma_izq_2=0
for i in range (len(matriz)):
  suma_izq_2=suma_izq_2+matriz[i][i]

print("La suma es: ",suma_izq_2)

suma_dere=0
for i in range (len(matriz)):
  suma_dere=suma_dere+matriz[i][(len(matriz)-1)-i]
print("ls suma Derecha es : ",suma_dere)

#=====================
matriz=[]
f0=[1,2,3,4]
f1=[5,6,7,8]
f2=[9,10,11,12]
f3=[13,14,15,16]
matriz.append(f0)
matriz.append(f1)
matriz.append(f2)
matriz.append(f3)

for f in range(len(matriz)):
  for c in range(len(matriz)):
    print(matriz[f][c],end="\t")
  print()
