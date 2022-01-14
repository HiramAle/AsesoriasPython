import numpy as np
import random


def bubble_sort(array: list):
    print(array)
    sorting = True

    while sorting:
        sorting = False
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                # aux = array[j]
                # array[j] = array[j + 1]
                # array[j + 1] = aux
                array[j], array[j + 1] = array[j + 1], array[j]
                sorting = True
    print(array)


def recursive_bb_sort(array: list, sorting=True):
    if sorting:
        sorting = False
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                # aux = array[j]
                # array[j] = array[j + 1]
                # array[j + 1] = aux
                array[j], array[j + 1] = array[j + 1], array[j]
                sorting = True
        recursive_bb_sort(array, sorting)
    return array


def binary_search(array: list, x: int, low: int, high: int):
    if high >= low:
        mid = (high + low) // 2
        if array[mid] == x:
            return mid
        elif x > array[mid]:
            return binary_search(array, x, mid + 1, high)
        else:
            return binary_search(array, x, low, mid - 1)
    else:
        return False


def fill():
    matrix = np.zeros((6, 7))
    for i in range(6):
        for j in range(7):
            matrix[i][j] = random.randint(0, 10)
    return matrix


def ex_numpy():
    animales = ["perros", "gatos", "conejos", "peces", "aves", "hurones"]
    matrix = fill()
    print(matrix)
    perros = matrix[0].argmax()
    print("El dia que se recibieron mas perros fue", perros)

    promedioGatos = matrix.sum(axis=1)[1] / 7
    print("El promedio de gatos fue", promedioGatos)

    mas = matrix.sum(axis=0).argmax()
    print("El dia que se recibieron mas mascotas fue", mas)

    animalMas = matrix.sum(axis=1).argmax()
    print("El animal que se recibio mas fue", animales[animalMas])




def main():
    numbers = [2, 76, 9, 10, 24, 100, 56, 1, 8, 33]
    # bubble_sort(numbers)
    # array_sorted = recursive_bb_sort(numbers)
    # print(array_sorted)
    # print(binary_search(numbers, 80, 0, len(array_sorted) - 1))

    ex_numpy()

    return


if __name__ == '__main__':
    main()
