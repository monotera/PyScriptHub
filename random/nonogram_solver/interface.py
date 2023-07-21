def printBoard(parametrosX, parametrosY, tamA, tablero):
    tamX = 0
    tamY = 0

    for i in range(tamA):
        auxX = len(parametrosX[i])
        auxY = len(parametrosY[i])
        if auxX > tamX:
            tamX = auxX
        # end if
        if auxY > tamY:
            tamY = auxY
        # end if

    maxY = tamY
    tamY = (tamY * 2) + 1

    for i in range(tamA + 1):
        if i == 0:
            print(" " * (tamY + 2), end="┌")
        elif i == tamA:
            print("─" * 5, end="┐")
        else:
            print("─" * 5, end="┬")

    print()

    for i in range(tamX):
        for j in range(tamA):
            if j == 0:
                if len(parametrosX[j]) > i:
                    print(" " * tamY, " | ", parametrosX[j][i], end="  | ")
                else:
                    print(" " * tamY, " |   ", end="  | ")
            else:
                if len(parametrosX[j]) > i:
                    print("", parametrosX[j][i], end="  | ")
                else:
                    print("  ", end="  | ")
        print()

    for i in range(tamA + 1):
        if i == 0:
            print("┌", end="")
            print("─" * (tamY + 1), end="┼")
        elif i == tamA:
            print("─" * 5, end="┤")
        else:
            print("─" * 5, end="┼")

    for i in range(tamA):
        print()
        for j in range(tamA):
            if j == 0:
                print(end="| ")
                for k in range(len(parametrosY[i])):
                    print(parametrosY[i][k], end=" ")

                if maxY == len(parametrosY[i]):
                    ope = maxY - len(parametrosY[i]) - 1
                else:
                    ope = tamY - (len(parametrosY[i]) * 2) - 1
                # end if
                print(" " * ope, end=" | ")

            print(tablero[i][j], end=" | ")

        print()

        for j in range(tamA + 1):
            if j == 0:
                if i == tamA - 1:
                    print("└", end="")
                    print("─" * (tamY + 1), end="┴")
                else:
                    print("├", end="")
                    print("─" * (tamY + 1), end="┼")
            elif i == tamA - 1 and j == tamA:
                print("─" * 5, end="┘")
            elif j == tamA:
                print("─" * 5, end="┤")
            else:
                if i == tamA - 1:
                    print("─" * 5, end="┴")
                else:
                    print("─" * 5, end="┼")

    print()
