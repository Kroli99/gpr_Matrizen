with open("test_matrix_10.txt", "r") as file:
    matrix = []
    matrix_int = []
    for line in file:
        if len(line.split(" ")) <= 2:
            continue
        elif len(line.split(" ")) > 2:
            matrix.append(line.strip().split(" "))

    for i in range(len(matrix)):
        row=[]
        for j in range(len(matrix[0])):
            row.append(int(matrix[i][j]))
        matrix_int.append(row)
    print(matrix_int)

with open("test_matrix_10.txt", "r") as file:
    matrix = []
    for line in file:
        print(file.readlines())

