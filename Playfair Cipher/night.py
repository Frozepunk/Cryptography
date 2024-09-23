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

def find_position(matrix, letter):
    for r, row in enumerate(matrix):
        if letter in row:
            return r, row.index(letter)
    return None

def preprocess_text(text):
    text = text.lower()
    processed_text = []
    i = 0
    while i < len(text):
        processed_text.append(text[i])
        if i + 1 < len(text) and text[i] == text[i + 1]:
            processed_text.append('x') 
    if len(processed_text) % 2 != 0:
        processed_text.append('x') 
    return processed_text

def postprocess_text(text):
    processed_text = []
    i = 0
    while i < len(text):
        processed_text.append(text[i])
        if i + 1 < len(text) and text[i] == text[i + 1] and text[i+1] == 'x':
            i += 1
        i += 1
    return ''.join(processed_text)

def playfair_cipher(matrix, text, mode='encrypt'):
    processed_text = preprocess_text(text)
    pairs = []
    result = []
    
    for i in range(0, len(processed_text), 2):
        a, b = processed_text[i], processed_text[i + 1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)
        if r1 is None or r2 is None:
            raise ValueError(f"Letter '{a}' or '{b}' not found in the matrix.")
        if r1 == r2:
            if mode == 'encrypt':
                new_a = matrix[r1][(c1 + 1) % 5]
                new_b = matrix[r2][(c2 + 1) % 5]
            else:  # decryption
                new_a = matrix[r1][(c1 - 1) % 5]
                new_b = matrix[r2][(c2 - 1) % 5]
        elif c1 == c2:
            if mode == 'encrypt':
                new_a = matrix[(r1 + 1) % 5][c1]
                new_b = matrix[(r2 + 1) % 5][c2]
            else:  # decryption
                new_a = matrix[(r1 - 1) % 5][c1]
                new_b = matrix[(r2 - 1) % 5][c2]
        else:
            new_a = matrix[r1][c2]
            new_b = matrix[r2][c1]
        
        pairs.append(((a, b), (new_a, new_b)))
        result.append(new_a)
        result.append(new_b)
    
    decrypted_text = ''.join(result)
    if mode == 'decrypt':
        decrypted_text = postprocess_text(decrypted_text)
    
    return pairs, decrypted_text

# Main code
keyword = input("Enter a keyword: ")
matrix_5x5 = create_5x5_matrix(keyword)
print("Playfair Cipher Matrix:")
for row in matrix_5x5:
    print(" ".join(row))

text = input("Enter the text to encrypt: ")
pairs, encrypted_text = playfair_cipher(matrix_5x5, text, mode='encrypt')
print("Encrypted text:", encrypted_text)
print("Matching pairs (original -> encrypted):")
for original_pair, encrypted_pair in pairs:
    print(f"{original_pair} -> {encrypted_pair}")

pairs, decrypted_text = playfair_cipher(matrix_5x5, encrypted_text, mode='decrypt')
print("Decrypted text:", decrypted_text)
print("Matching pairs (encrypted -> original):")
for encrypted_pair, original_pair in pairs:
    print(f"{encrypted_pair} -> {original_pair}")
