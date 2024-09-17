def create_5x5_matrix(keyword):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    keyword = "".join(dict.fromkeys(keyword.lower()))
    matrix = []
    for letter in keyword:
        if letter in alphabet and letter not in matrix:
            matrix.append(letter)
    for letter in alphabet:
        if letter not in matrix:
            matrix.append(letter)
    matrix_5x5 = [matrix[i:i + 5] for i in range(0, 25, 5)]
    
    return matrix_5x5
keyword = input("Enter a keyword: ")
matrix_5x5 = create_5x5_matrix(keyword)
for row in matrix_5x5:
    print(" ".join(row))
