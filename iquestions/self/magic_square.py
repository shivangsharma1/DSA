def check_magic_square(matrix):

    row, col = len(matrix), len(matrix[0])
    diag1 , diag2 = 0, 0

    for i in range(row):
        diag1 += matrix[i][i]
        diag2 += matrix[i][row-i-1]

    if diag1!=diag2:
        return 0
    
    hashset = []
    rowsum, colsum = 0, 0
    for i in range(row):
        rowsum, colsum = 0, 0
        for j in range(col):
            rowsum+=matrix[i][j]
            colsum+=matrix[j][i]
        print("rowsum: ",rowsum)
        print("colsum", colsum)
        hashset.append(rowsum)
        hashset.append(colsum)
    print(hashset)
    print(diag1)
    print(diag2)
    if len(set(hashset)) == 1 and hashset[0] == diag1 == diag2:
        return 1
    else:
        return 0





if __name__ == '__main__':
    mat = [[ 2, 7, 6 ],[ 9, 5, 1 ],[ 4, 3, 8 ]]

    print(check_magic_square(mat))