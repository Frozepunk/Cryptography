def create_matrix(keyword):
    keyword = ''.join(dict.fromkeys(keyword.lower().replace('j', 'i')))
    alphabet = 'abcdefghiklmnopqrstuvwxyz'
    matrix = keyword + ''.join([c for c in alphabet if c not in keyword])
    return [matrix[i:i + 5] for i in range(0, 25, 5)]

def find_position(matrix, letter):
    for r, row in enumerate(matrix):
        if letter in row:
            return r, row.index(letter)

def preprocess_text(text):
    text = text.lower().replace('j', 'i')
    result = []
    for i in range(len(text)):
        result.append(text[i])
        if i + 1 < len(text) and text[i] == text[i + 1]:
            result.append('x')
    if len(result) % 2:
        result.append('x')
    return result

def playfair_cipher(matrix, text, mode='encrypt'):
    processed_text = preprocess_text(text)
    result = []
    step = 1 if mode == 'encrypt' else -1

    for i in range(0, len(processed_text), 2):
        a, b = processed_text[i], processed_text[i + 1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)
        if r1 == r2:
            result.extend([matrix[r1][(c1 + step) % 5], matrix[r2][(c2 + step) % 5]])
        elif c1 == c2:
            result.extend([matrix[(r1 + step) % 5][c1], matrix[(r2 + step) % 5][c2]])
        else:
            result.extend([matrix[r1][c2], matrix[r2][c1]])

    return ''.join(result)

# Main Code
keyword = input("Enter a keyword: ")
matrix = create_matrix(keyword)
print("Matrix:")
for row in matrix:
    print(' '.join(row))

text = input("Enter text to encrypt: ")
encrypted = playfair_cipher(matrix, text, 'encrypt')
print("Encrypted text:", encrypted)

decrypted = playfair_cipher(matrix, encrypted, 'decrypt')
print("Decrypted text:", decrypted)
