mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]


def rotate_metrix(metrix):
    for i in range(len(metrix)):
        metrix[i].reverse()
        
    for i in range(len(metrix)):
        for j in range(i, len(metrix)):
            metrix[i][j] , metrix[j][i] = metrix[j][i], metrix[i][j]
rotate_metrix(mat)


def display_metrix(metrix):
    for i in range(len(metrix)):
        for j in range(len(metrix)):
            print(metrix[i][j], end = " ")
        print()

display_metrix(mat)
            