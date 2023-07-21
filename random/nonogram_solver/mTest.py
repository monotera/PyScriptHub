import json
from interface import *
import pprint
import random
import sys

boards = []
mainBoard = -1
gameBoard = [[]]
intentos = 0
gameOver = False


def loadData(filename):
    with open(filename) as jsonFile:
        boards = json.load(jsonFile)
        jsonFile.close()
    return boards


def __init__():
    global boards
    boards = loadData("data.json")
    # print("Datos cargados!")
    # print("Buena suerte!")
    menu()


def menu():
    global gameOver

    while not gameOver:
        # print("\nMENU PRINCIPAL: \n")
        # print("1. Escoger tablero")
        # print("2. Reglas del juego")
        # print("3. Puntuaciones")
        # print("4. Salir")

        # opt = int(input("\nSeleccione una opcion: "))
        opt = 1

        if opt == 1:
            boardsMenu()
        # end if
        if opt == 2:
            rules()
        # end if
        if opt == 3:
            topTimes()
        # end if
        if opt == 4:
            endGame()
            break
        # end if


# end def


def boardsMenu():
    global boards, mainBoard, gameBoard
    # print("\nBOARDS MENU: \n")
    """
    for i in range(len(boards)):
        print("Tablero: ",i+1, "Tamanio: ", boards[i]['tamanio'], "Dificultad: ", boards[i]['dificultad'])
    """
    while True:
        # opc = int(input("Seleccione un tablero: "))
        # print(sys.argv)
        opc = 7

        if opc > 1 or opc < len(boards):
            mainBoard = opc
            break
        """
        else:
            print("Opcion no valida, intente de nuevo")
        """

    tam = boards[opc - 1]["tamanio"]
    gameBoard = [[" " * 3 for i in range(tam)] for j in range(tam)]
    # printBoard(boards[opc-1]['parametrosX'], boards[opc-1]['parametrosY'], tam, gameBoard)

    game(boards[opc - 1])


def fillCell(board):
    global gameBoard, intentos, gameOver, mainBoard
    tam = int(board["tamanio"])
    opc = ""

    while True:
        # opc = input("Desea agregar una X(X), llenar una celda (F), limpiar una celda (D): ")
        opc = "F"

        if opc != "X" and opc != "F" and opc != "D":
            # print("Ingrese la opcion nuevamente")
            continue
        else:
            break

    cent = True

    while cent:
        cent = False
        # col = int(input("Ingrese el numero de la columna: "))
        # row = int(input("Ingrese el numero de la fila: "))
        col = random.randint(0, tam - 1)
        row = random.randint(0, tam - 1)

        if col < 0 or col > tam:
            # print("Se ingresaron mal las columnas")
            cent = True
        if row < 0 or row > tam:
            # print("Se ingresaron mal las filas")
            cent = True

        if gameBoard[row][col] == "███":
            # print("La posición se encuentra ocupada")
            cent = True

    if opc == "X":
        gameBoard[row][col] = " X "
    elif opc == "F":
        gameBoard[row][col] = "███"
    else:
        gameBoard[row][col] = "   "

    isValid = checkBoard(board, gameBoard, tam, col, row)

    if not isValid:
        isOver = False
        gameBoard[row][col] = "   "
        # print("No Se pudo hacer el movimiento")
        intentos = intentos + 1
        if intentos == 10:
            isOver = validarSolucionesRestantes(board, gameBoard, tam)

            if isOver:
                # print("Fin del juego")

                gana = validateGameboard(board, tam)
                """
                if(gana):
                    print("Gana")
                else:
                    print("Pierde")
                """

                with open("data" + str(mainBoard) + ".txt", "a") as text_file:
                    text_file.write(str(gana) + "\n")

                gameOver = True
            else:
                intentos = 0

    # printBoard(board['parametrosX'], board['parametrosY'], tam, gameBoard)

    game(board)


def game(board):
    global gameBoard, mainBoard, gameOver

    if not gameOver:
        tam = boards[mainBoard - 1]["tamanio"]

        baseListY, baseListX = findBaseElements(board, gameBoard, tam)

        for i in range(len(baseListX)):
            fillBaseGameBoard(
                baseListX[i], "row", board["parametrosY"][baseListX[i]], tam
            )

        for i in range(len(baseListY)):
            fillBaseGameBoard(
                baseListY[i], "col", board["parametrosX"][baseListY[i]], tam
            )

        # print("\nCargando solución base...\n")

        # printBoard(board['parametrosX'], board['parametrosY'], tam, gameBoard)
        # opc = input("Desea continuar con el juego? S/N ")

        opc = "S"
        fillCell(board)
    else:
        # print("Su tiempo fue de: ")
        tam = board["tamanio"]
        gameBoard = [[" " * 3 for i in range(tam)] for j in range(tam)]
        menu()


def checkBoard(board, gameBoard, tam, col, row):
    parY = board["parametrosX"][col]
    parX = board["parametrosY"][row]

    listY = []
    listX = []
    contarY = False
    contarX = False
    contadorY = 0
    contadorX = 0
    validacionY = []
    validacionX = []

    for i in range(tam):
        if gameBoard[i][col] == "███":
            contadorY += 1
            contarY = True

        if gameBoard[i][col] == "   " and contarY == True:
            listY.append(contadorY)
            contadorY = 0
            contarY = False

        if gameBoard[row][i] == "███":
            contadorX += 1
            contarX = True

        if gameBoard[row][i] == "   " and contarX == True:
            listX.append(contadorX)
            contadorX = 0
            contarX = False

    if contadorY != 0:
        listY.append(contadorY)

    if contadorX != 0:
        listX.append(contadorX)

    faltantesX = len(parX) - len(listX)
    if faltantesX > 0:
        for i in range(faltantesX):
            listX.append(0)

    faltantesY = len(parY) - len(listY)
    if faltantesY > 0:
        for i in range(faltantesY):
            listY.append(0)

    for i in range(len(parY)):
        if listY[i] > parY[i]:
            validacionY.append(False)
        else:
            validacionY.append(True)

    for i in range(len(parX)):
        if listX[i] > parX[i]:
            validacionX.append(False)
        else:
            validacionX.append(True)

    isValid = True

    if False in validacionX or False in validacionY:
        isValid = False

    return isValid


def validarSolucionesRestantes(board, gameBoard, tam):
    isOver = True
    isValid = []

    for i in range(tam):
        for j in range(tam):
            if gameBoard[i][j] == "   ":
                gameBoard[i][j] = "███"
                isValid.append(checkBoard(board, gameBoard, tam, j, i))
                gameBoard[i][j] = "   "

    if True in isValid:
        isOver = False

    return isOver


def findBaseElements(board, gameBoard, tam):
    parY = board["parametrosX"]
    parX = board["parametrosY"]

    baseY = []
    baseX = []

    for i in range(tam):
        sumY = 0
        sumX = 0
        for j in range(len(parY[i])):
            sumY += parY[i][j]
            if len(parY[i]) - 1 > j:
                sumY += 1

        for j in range(len(parX[i])):
            sumX += parX[i][j]
            if len(parX[i]) - 1 > j:
                sumX += 1

        if sumY == tam:
            baseY.append(i)

        if sumX == tam:
            baseX.append(i)

    return baseY, baseX


def fillBaseGameBoard(num, direction, param, tam):
    global gameBoard

    if direction == "col":
        k = 0
        contador = param[k]
        for i in range(tam):
            if contador != 0:
                gameBoard[i][num] = "███"
                contador -= 1
            else:
                k += 1
                contador = param[k]

    if direction == "row":
        k = 0
        contador = param[k]
        for i in range(tam):
            if contador != 0:
                gameBoard[num][i] = "███"
                contador -= 1
            else:
                k += 1
                contador = param[k]


def validateGameboard(board, tam):
    global gameBoard

    parY = board["parametrosX"]
    parX = board["parametrosY"]

    whiteRows = []

    cent = True

    for i in range(tam):
        totalSupuestoX = sum(parX[i])
        totalRealX = gameBoard[i].count("███")

        totalSupuestoY = sum(parY[i])
        col = column(gameBoard, i)
        totalRealY = col.count("███")

        if totalRealX != totalSupuestoX or totalRealY != totalSupuestoY:
            cent = False

    return cent


def column(matrix, i):
    return [row[i] for row in matrix]


def rules():
    print("\nREGLAS: \n")
    print("=================================OBJETIVO=================================")
    print("= El objetivo del juego es rellenar la cuadrícula con cuadrados negros   =")
    print("= para que los números de cuadrados secuenciales rellenos coincidan con  =")
    print("= los números en la parte superior e izquierda.                          =")
    print("==========================================================================")
    print()
    print("==============================¿COMO EMPEZAR?==============================")
    print("= 1. Al iniciar el juego se cargan los parametros del archivo data.json. =")
    print("= 2. Existen tres posibles movimientos para los tableros cargados:       =")
    print("=           - X: Para marcar con una equis una celda.                    =")
    print("=           - F: Para llenar una celda.                                  =")
    print("=           - D: Para limpiar una celda.                                 =")
    print("= 3. Al momento de seleccionar N senialando que no va a continuar el     =")
    print("=   juego, el tablero sera borrado.                                      =")
    print("= 4. Para terminar con la ejecucion del juego basta con seleccionar la   =")
    print("=   de salir en el menu principal.                                       =")
    print("==========================================================================")


def topTimes():
    print("en construccion")


def endGame():
    print("Gracias por jugar!")
    exit()


__init__()
