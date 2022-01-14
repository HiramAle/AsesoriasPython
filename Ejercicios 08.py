import math

def recursive_print_image(image: list, row=0, column=0):
    if row < len(image):
        if column < len(image):
            if image[row][column] == 1:
                print("██", end="")
            else:
                print("  ", end="")
            recursive_print_image(image, row, column + 1)
        else:
            print()
            recursive_print_image(image, row + 1, 0)


def recursive_invert_image(image: list, row=0, column=0):
    if row < len(image):
        if column < len(image[0]):
            if image[row][column] == 1:
                image[row][column] = 0
            elif image[row][column] == 0:
                image[row][column] = 1
            recursive_invert_image(image, row, column + 1)
        else:
            recursive_invert_image(image, row + 1, 0)
    return image


def diagonalSum(matrix: list):
    suma = 0
    for i in range(len(matrix)):
        suma += matrix[i][i]
        suma += matrix[i][len(matrix) - 1 - i]

    if len(matrix) % 2 > 0:
        suma -= matrix[len(matrix) // 2][len(matrix) // 2]

    print(suma)




def main():
    blackSquare = "██"

    image = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
             [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
             [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0],
             [0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0],
             [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
             [1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
             [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
             [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
             [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    # recursive_print_image(image)
    # recursive_print_image(recursive_invert_image(image))

    pairDiagonalMatrix = [[1, 6, 3, 2],
                          [7, 2, 5, 7],
                          [2, 6, 7, 5],
                          [9, 2, 4, 1]]

    oddDiagonalMatrix = [[2, 4, 1],
                         [9, 4, 7],
                         [7, 4, 6]]

    diagonalSum(oddDiagonalMatrix)

    return


if __name__ == '__main__':
    main()
