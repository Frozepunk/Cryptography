
# how to read a keyword and split into a 5x5 matrix and fill the remaining words with alphabets and removing the duplicate words
keyword = input("Enter the keyword: ")
keyword = ''.join(sorted(set(keyword), key=keyword.index))
matrix = [list(keyword)]
for i in range(25 - len(keyword)):
    if chr(65 + i) not in keyword:
        matrix[0].append(chr(65 + i))
for i in range(4):
    matrix.append([])
    for j in range(5):
        matrix[i + 1].append(chr(65 + 5 * i + j))
        if chr(65 + 5 * i + j) in keyword:
            matrix[i + 1][j] = ''
print(matrix)
# how to read a keyword and split into a 5x5 matrix and fill the remaining words with alphabets and removing the duplicate words 