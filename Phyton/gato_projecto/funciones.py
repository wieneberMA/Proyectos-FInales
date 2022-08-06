import random as rd
import os, sys,time
import platform as pt
#///////////////////////////////////////////////////////
def menu():
  tablero = [["1", "2", "3"], ["4", "X", "6"], ["7", "8", "9"]]
  while True:
    menu = {}
    menu[1]="juego nuevo"
    menu[2]="salir"
    for i in menu:
      print("\n",i,".-",menu[i])
    while True:
      salida = int(input("\n->"))
      if salida > 3 or salida < 1:
        print("numero no valido")
      else:
        operation(tablero,salida)
        break
    break
#////////////////////////////////////////////////////////////////
def operation(tablero,op):
  if op == 1:
    while True:
      DisplayBoard(tablero)
      EnterMove(tablero)
      VictoryFor(tablero)
      DrawMove(tablero)
      MakeListOfFreeFields(tablero)

  if op == 2:
    sys.exit()



#////////////////////////////////////////////////////////////////

#def DisplayBoard(board):
#
# la función acepta un parámetro el cual contiene el estado actual del tablero
# y lo muestra en la consola
def DisplayBoard(tablero):
  print(str(tablero[0][0]) + "|" + str(tablero[0][1]) + "|" + str(tablero[0][2]))
  print("-----")
  print(str(tablero[1][0]) + "|" + str(tablero[1][1]) + "|" + str(tablero[1][2]))
  print("-----")
  print(str(tablero[2][0]) + "|" + str(tablero[2][1]) + "|" + str(tablero[2][2]))
#//////////////////////////////////////////////////////////////////
#def EnterMove(board):
# la función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,
# verifica la entrada y actualiza el tablero acorde a la decisión del usuario
def EnterMove(tablero):
  movimiento = input("\n introdusca su movimiento -> ")
  if movimiento == 5:
    print("lugar ya ocupado")
    EnterMove(tablero)
  for i in range(0, 2 + 1):
    for j in range(0, 2 + 1):
      if movimiento in tablero[i][j]:
        if "X" in tablero[i][j] or "O" in tablero[i][j]:
          print("espacio ya colocado")
          EnterMove(tablero)
        tablero[i].pop(j)
        tablero[i].insert(j, "O")
#/////////////////////////////////////////////////////////////////////
def MakeListOfFreeFields(tablero):
  #
  # la función examina el tablero y construye una lista de todos los cuadros vacíos
  # la lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna
  #  tablero = [["1","2","3"],["4","X","6"],["7","8","9"]]
  #
  tupla = ()
  lista = []
  for i in range(0, 2 + 1):
    for j in range(0, 2 + 1):
      for x in range(1,9+1):
        if tablero[i][j] == str(x):
          lista.append((i,j))
  if not lista:
    print("juego empate")
    menu()
  print(lista)
#
#//////////////////////////////////////////////////////////////////////////////
#def VictoryFor(board, sign):
#
# la función analiza el estatus del tablero para verificar si
# el jugador que utiliza las 'O's o las 'X's ha ganado el juego
def VictoryFor(tablero):
  if tablero[0][0] == "O" and tablero[1][0] == "O" and tablero[2][0] == "O" or \
     tablero[0][2] == "O" and tablero[1][2] == "O" and tablero[2][2] == "O" or \
     tablero[2][0] == "O" and tablero[2][1] == "O" and tablero[2][2] == "O" or \
     tablero[0][0] == "O" and tablero[0][1] == "O" and tablero[0][2] == "O":
    print("ganador O")
    sys.exit()
  if tablero[0][1] == "X" and tablero[0][0] == "X" and tablero[0][2] == "X" or \
     tablero[1][0] == "X" and tablero[1][1] == "X" and tablero[1][2] == "X" or \
     tablero[2][0] == "X" and tablero[2][1] == "X" and tablero[2][2] == "X" or \
     tablero[2][0] == "X" and tablero[1][1] == "X" and tablero[0][2] == "X" or \
     tablero[0][0] == "X" and tablero[1][1] == "X" and tablero[2][2] == "X" or \
     tablero[0][0] == "X" and tablero[1][0] == "X" and tablero[2][0] == "X" or \
     tablero[0][1] == "X" and tablero[1][1] == "X" and tablero[2][1] == "X" or \
     tablero[0][2] == "X" and tablero[1][2] == "X" and tablero[2][2] == "X":
    print("ganador X")
    sys.exit()
#//////////////////////////////////////////////////////////////////////////////
#def DrawMove(board):
# la función dibuja el movimiento de la maquina y actualiza el tablero
def DrawMove(tablero):
  while True:
    bot = 0
    bot = rd.randint(1,10)
    if bot == 5:
      DrawMove(tablero)
    else:
      for i in range(0, 2 + 1):
        for j in range(0, 2 + 1):
          if str(bot) in tablero[i][j]:
            if tablero[i][j] =="X" or tablero[i][j] =="O":
              DrawMove(tablero)
            tablero[i].pop(j)
            tablero[i].insert(j,"X")
    break