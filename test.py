with open("test_matrix_10.txt", "r") as file:
    matrix = [line.strip().split(" ") for line in file if len(line.split(" ")) > 2]
#    for line in file:
#        if len(line.split(" ")) <= 2:
#            continue
#        elif len(line.split(" ")) > 2:
#            matrix.append(line.strip().split(" "))
    print(matrix)
