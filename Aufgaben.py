import timeit

M = ([[1, 0, 3], [0, 2, 4]])
a = (2, 3, [1, 0, 3, 0, 2, 4])


# Matrix als Liste von Listen
def well_formed_matrix(m):
    prev_len = None
    for i in range(len(m)):
        if len(m[i]) == 0 or (i > 0 and len(m[i]) != prev_len):
            return False
        prev_len = len(m[i])
    return True


print(well_formed_matrix(M))


# Matrix als Liste von Listen transponieren
def transpose_list(m):
    result = []
    for j in range(len(m[0])):
        row = []
        for i in range(len(m)):
            row.append(m[i][j])
        result.append(row)
    return result


print(transpose_list(M))


# Matrix flach in einer Liste
def flatten(m):
    lst = []
    row = len(m)
    columns = len(m[0])
    tupl = (row, columns, lst)
    for i in range(len(m)):
        for j in range(len(m[0])):
            lst.append(m[i][j])
    return tupl


print(flatten(M))


# Transponier-Funktion erweitern
def transpose_tuple(m):
    list = m[2]
    matrix = [list[:m[1]], list[m[1]:]]
    result = []
    for j in range(len(matrix[0])):
        row = []
        for i in range(len(matrix)):
            row.append(matrix[i][j])
        result.append(row)
    return result


def transpose_erweitert(m):
    if type(m) == list:
        return transpose_list(m)
    elif type(m) == tuple:
        return transpose_tuple(m)


print(transpose_erweitert(a))


# Matrix als Dictionary
def as_dict(m):
    d = {}
    row = len(m)
    columns = len(m[0])
    tupl = (row, columns, d)
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 0:
                continue
            else:
                d[(i, j)] = m[i][j]
    return tupl


print(as_dict(M))


# Transponier-Funktion nochmals erweitern

# Addition von Matrizen
def mat_add(m1, m2):
    if (type(m1) == list and type(m2) == list) and len(m1) == len(m2):
        ms_list = []
        for i in range(len(m1)):
            lst = []
            for j in range(len(m1[0])):
                lst.append(m1[i][j] + m2[i][j])
            ms_list.append(lst)
        return ms_list

    if (type(m1) == tuple and type(m2) == tuple) and m1[:2] == m2[:2]:
        first = m1[2]
        second = m2[2]
        tuple_list = []
        tupl = (m1[0], m1[1], tuple_list)
        for i in range(len(first)):
            tuple_list.append(first[i] + second[i])
        return tupl


#    if (type(m1) == dict and type(m2) == dict) and m1[:2] == m2[:2]:

print(mat_add(a, a))


# Multiplikation von Matrizen
def mat_mul(m1, m2):
    if (type(m1) == list and type(m2) == list) and len(m1) == len(m2):
        result = []
        for i in range(len(m1)):
            row = []
            for j in range(len(m1[0])):
                row.append(m1[i][j] * m2[i][i])
            result.append(row)
        return result



print(timeit.timeit(stmt="mat_add(M, M)", setup="", number=1, globals=globals()))

matrix_file = "test_matrix_10.txt"
def read_matrix(file_name):
    with open(file_name, "r") as file:
        matrix = [line.strip().split(" ") for line in file if len(line.split(" ")) > 2]
        matrix_int = [[int(matrix[i][j]) for j in range(len(matrix[0]))] for i in range(len(matrix))]
        return matrix_int


print(timeit.timeit(stmt="mat_add(read_matrix(matrix_file), read_matrix(matrix_file))", setup="", number=1, globals=globals()))

tuple_time = 0.00013410000000002587
list_time = 0.00023980000000001223
