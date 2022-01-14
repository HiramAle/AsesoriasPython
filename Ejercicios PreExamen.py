import random
import numpy as np
import pandas as pd


def diagonal_validation(matrix: list, diagonal_sum):
    suma = 0
    for i in range(len(matrix)):
        if matrix[i][i] == 1 and matrix[i][len(matrix) - 1 - i] == 1:
            suma += matrix[i][i]
            suma += matrix[i][len(matrix) - 1 - i]
        else:
            return False

    if len(matrix) % 2 > 0:
        suma -= matrix[len(matrix) // 2][len(matrix) // 2]

    if suma == diagonal_sum:
        return True
    else:
        return False


def scalar_mult(matrix: list, scalar: int, row=0, column=0):
    if row < len(matrix):
        if column < len(matrix[0]):
            matrix[row][column] = matrix[row][column] * scalar
            scalar_mult(matrix, scalar, row, column + 1)
        else:
            scalar_mult(matrix, scalar, row + 1, 0)
    return matrix


def numpy_ex():
    matrix = np.empty((20, 9))
    columns = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre"]

    for i in range(20):
        for j in range(9):
            matrix[i][j] = round(random.uniform(0, 500), 2)

    print(pd.DataFrame(data=matrix, columns=columns))

    uno = matrix.sum(axis=1).argmin()
    print("La cuenta que menos gastó fue", uno)

    dos = matrix.sum(axis=0)[1] / 20
    print("El gasto promedio en Febrero fue", dos)

    c2 = matrix[1][6]
    c8 = matrix[7][6]
    if c2 > c8:
        tres = "cuenta 2"
    else:
        tres = "cuenta 8"
    print("Entre la cuenta 2 y 8, la que gasto mas en julio fue la", tres)

    cuatro = 0
    for i in range(2, 6):
        cuatro += matrix[14][i] + matrix[15][i]
    print("Entre el mes de Marzo a Junio, las cuentas 15 y 16 gastaron $", cuatro)


def main():
    matrix = [[1, 9, 5, 3, 1],
              [2, 1, 3, 1, 0],
              [3, 6, 1, 8, 7],
              [2, 1, 3, 1, 6],
              [1, 4, 8, 3, 1]]
    # print(diagonal_validation(matrix, 9))

    # print(scalar_mult(matrix, 2))

    numpy_ex()

    return


if __name__ == '__main__':
    main()
