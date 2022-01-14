import random
import numpy as np


def simetrica(mat: list, d: int):
    aux = 1
    for i in range(0, d - 1):
        for j in range(aux, d):
            print(mat[i][j])
            if mat[i][j] != mat[j][i]:
                return False
        aux += 1
    return True


def triangularInferior(mat: list, d1: int, d2: int, r: int):
    if d1 > 0:
        if d2 > 0:
            print(mat[d1 - 1][d2 - 1])
            triangularInferior(mat, d1, d2 - 1, r)
        else:
            triangularInferior(mat, d1 - 1, r - 1, r - 1)


def lower_triangular(matrix: list, row: int, column: int):
    if row > 0:
        if column > 0:
            if matrix[row - 1][column - 1] != 0:
                print(matrix[row - 1][column - 1], end=" ")
            lower_triangular(matrix, row, column - 1)
        else:
            print()
            lower_triangular(matrix, row - 1, len(matrix))


def lower_triangular2(matrix: list, row: int, column: int):
    if row > 0:
        if column > 0:
            if matrix[len(matrix) - row][len(matrix) - column] != 0:
                print(matrix[len(matrix) - row][len(matrix) - column], end=" ")
            lower_triangular2(matrix, row, column - 1)
        else:
            print()
            lower_triangular2(matrix, row - 1, len(matrix))


def deforestacion():
    matriz = np.zeros((7, 12))
    for i in range(7):
        for j in range(12):
            matriz[i][j] = random.randint(1, 100)
    print(matriz)
    sumasFilas = matriz.sum(axis=1)
    index = sumasFilas.argmax()
    number = sumasFilas[index]
    print("El pais mas dañado fue", index, "perdió:", number)

    sumasColumnas = matriz.sum(axis=0)
    losses = sumasColumnas[5] + sumasColumnas[6]
    print("En junio y julio se perdió", losses)





def main():
    # Matriz Triangular
    matriz = [[1, 0, 0, 0],
              [5, 6, 0, 0],
              [4, 1, 8, 0],
              [2, 7, 9, 5]]
    # triangularInferior(matriz, 4, 4, 4)
    lower_triangular(matriz, 4, 4)
    lower_triangular2(matriz, 4, 4)
    # Matriz Simetrica
    matriz_sim = [[0, 1, 2, 3],
                  [1, 0, 4, 5],
                  [2, 4, 0, 6],
                  [3, 5, 6, 0]]
    # print(simetrica(matriz_sim, 4))
    # deforestacion()
    return


if __name__ == '__main__':
    main()
