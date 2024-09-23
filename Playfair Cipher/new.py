import string

def create_matrix(key):
    key = key.replace("J", "I").upper()
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Note 'J' is omitted
    matrix = []
    
    # Remove duplicates from the key
    seen = set()
    for char in key:
        if char not in seen and char in alphabet:
            seen.add(char)
            matrix.append(char)

    # Add remaining letters of the alphabet
    for char in alphabet:
        if char not in seen:
            matrix.append(char)

    return [matrix[i:i + 5] for i in range(0, 25, 5)]

def preprocess_text(text):
    text = text.replace("J", "I").upper()
    processed = ""
    
    i = 0
    while i < len(text):
        char = text[i]
        if char in string.ascii_uppercase:
            processed += char
            if i + 1 < len(text):
                if text[i + 1] == char:  # Duplicate letters
                    processed += 'X'
                else:
                    processed += text[i + 1]
                    i += 1
        i += 1
    return processed

def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return None

def encrypt(key, plaintext):
    matrix = create_matrix(key)
    plaintext = preprocess_text(plaintext)
    ciphertext = ""

    for i in range(0, len(plaintext), 2):
        a, b = plaintext[i], plaintext[i + 1]
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)

        if row_a == row_b:  # Same row
            ciphertext += matrix[row_a][(col_a + 1) % 5]
            ciphertext += matrix[row_b][(col_b + 1) % 5]
        elif col_a == col_b:  # Same column
            ciphertext += matrix[(row_a + 1) % 5][col_a]
            ciphertext += matrix[(row_b + 1) % 5][col_b]
        else:  # Rectangle
            ciphertext += matrix[row_a][col_b]
            ciphertext += matrix[row_b][col_a]

    return ciphertext

def decrypt(key, ciphertext):
    matrix = create_matrix(key)
    plaintext = ""

    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i + 1]
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)

        if row_a == row_b:  # Same row
            plaintext += matrix[row_a][(col_a - 1) % 5]
            plaintext += matrix[row_b][(col_b - 1) % 5]
        elif col_a == col_b:  # Same column
            plaintext += matrix[(row_a - 1) % 5][col_a]
            plaintext += matrix[(row_b - 1) % 5][col_b]
        else:  # Rectangle
            plaintext += matrix[row_a][col_b]
            plaintext += matrix[row_b][col_a]

    return plaintext

# Example usage:
key = "hello"
plaintext = "jumbal"
ciphertext = encrypt(key, plaintext)
decrypted_text = decrypt(key, ciphertext)

print("Ciphertext:", ciphertext)
print("Decrypted Text:", decrypted_text)
