# import numpy as np
# from sympy import Matrix

# def letter_to_num(letter):
#     return ord(letter.upper()) - ord('A')

# def num_to_letter(num):
#     return chr((num % 26) + ord('A'))

# def encrypt_block(plain_block, key_matrix):
#     print(f"\nEncrypting block: {plain_block}")
#     plain_numbers = [letter_to_num(c) for c in plain_block]
#     print(f"Corresponding numbers for block '{plain_block}': {plain_numbers}")

#     result = np.dot(key_matrix, plain_numbers) % 26
#     print(f"Matrix multiplication result (mod 26): {result}")

#     encrypted_block = ''.join([num_to_letter(num) for num in result])
#     print(f"Encrypted block: {encrypted_block}")
    
#     return encrypted_block

# def decrypt_block(cipher_block, key_matrix_inverse):
#     print(f"\nDecrypting block: {cipher_block}")
#     cipher_numbers = [letter_to_num(c) for c in cipher_block]
#     print(f"Corresponding numbers for block '{cipher_block}': {cipher_numbers}")

#     result = np.dot(key_matrix_inverse, cipher_numbers) % 26
#     print(f"Matrix multiplication result (mod 26): {result}")

#     decrypted_block = ''.join([num_to_letter(num) for num in result])
#     print(f"Decrypted block: {decrypted_block}")
    
#     return decrypted_block

# def hill_cipher_encrypt(plaintext, key_matrix):
#     block_size = key_matrix.shape[0]
    
#     if len(plaintext) % block_size != 0:
#         plaintext += 'X' * (block_size - len(plaintext) % block_size)
#     print(f"\nPadded plaintext: {plaintext}")

#     ciphertext = ''
#     for i in range(0, len(plaintext), block_size):
#         block = plaintext[i:i+block_size]
#         ciphertext += encrypt_block(block, key_matrix)
    
#     return ciphertext

# def determinant_manual(matrix):
#     if len(matrix) == 2:
#         return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
#     det = 0
#     for c in range(len(matrix)):
#         minor = [[matrix[r][cc] for cc in range(len(matrix)) if cc != c] for r in range(1, len(matrix))]
#         cofactor = ((-1) ** c) * matrix[0][c] * determinant_manual(minor)
#         det += cofactor
#     return det

# def hill_cipher_decrypt(ciphertext, key_matrix):
#     print("\n---- Decryption Breakdown ----\n")
    
#     determinant_val = determinant_manual(key_matrix.tolist())
#     print(f"Determinant of the key matrix (manual calculation): {determinant_val}")
    
#     try:
#         determinant_inverse = pow(determinant_val, -1, 26)
#         print(f"\nModular inverse of the determinant modulo 26: {determinant_inverse}")
#     except ValueError:
#         print(f"\nDeterminant {determinant_val} has no modular inverse modulo 26. Decryption cannot proceed.")
#         return ""
    
#     adjugate_matrix = np.round(np.linalg.inv(key_matrix) * determinant_val).astype(int)
#     print(f"\nAdjugate matrix (adjoint of key matrix):\n{adjugate_matrix}\n")
    
#     key_matrix_inverse = (determinant_inverse * adjugate_matrix) % 26
#     print(f"Inverse key matrix modulo 26:\n{key_matrix_inverse}\n")
    
#     block_size = key_matrix.shape[0]
#     plaintext = ''
#     print("Decrypting each block:\n")
#     for i in range(0, len(ciphertext), block_size):
#         block = ciphertext[i:i+block_size]
#         plaintext += decrypt_block(block, key_matrix_inverse)
    
#     return plaintext

# def display_key_matrix_alphabets(key_matrix):
#     print("\nCorresponding alphabets of the key matrix numbers:")
#     for row in key_matrix:
#         row_alphabets = [num_to_letter(num) for num in row]
#         print(" ".join(row_alphabets))

# def get_key_matrix(matrix_size):
#     print(f"\nEnter the key matrix of size {matrix_size}x{matrix_size}:")
#     key_matrix = []
#     for i in range(matrix_size):
#         row = list(map(int, input(f"Enter row {i+1} values separated by space: ").split()))
#         key_matrix.append(row)
#     key_matrix = np.array(key_matrix)
    
#     display_key_matrix_alphabets(key_matrix)
    
#     return key_matrix

# def main():
#     matrix_size = int(input("Enter the size of the key matrix: "))
#     key_matrix = get_key_matrix(matrix_size)
    
#     plaintext = input("Enter the plaintext: ").upper().replace(" ", "")
#     print(f"\nOriginal plaintext: {plaintext}")

#     ciphertext = hill_cipher_encrypt(plaintext, key_matrix)
#     print(f"\nEncrypted text: {ciphertext}\n")
    
#     decrypted_text = hill_cipher_decrypt(ciphertext, key_matrix)
#     if decrypted_text:
#         print(f"Decrypted text: {decrypted_text}\n")

# if __name__ == "__main__":
#     main()

import numpy as np

def letter_to_num(letter):
    return ord(letter.upper()) - ord('A')

def num_to_letter(num):
    return chr((num % 26) + ord('A'))

def encrypt_block(plain_block, key_matrix):
    print(f"\nEncrypting block: {plain_block}")
    plain_numbers = [letter_to_num(c) for c in plain_block]
    print(f"Corresponding numbers for block '{plain_block}': {plain_numbers}")

    result = np.dot(key_matrix, plain_numbers) % 26
    print(f"Matrix multiplication result (mod 26): {result}")

    encrypted_block = ''.join([num_to_letter(num) for num in result])
    print(f"Encrypted block: {encrypted_block}")
    
    return encrypted_block

def hill_cipher_encrypt(plaintext, key_matrix):
    block_size = key_matrix.shape[0]
    
    if len(plaintext) % block_size != 0:
        plaintext += 'X' * (block_size - len(plaintext) % block_size)
    print(f"\nPadded plaintext: {plaintext}")

    ciphertext = ''
    for i in range(0, len(plaintext), block_size):
        block = plaintext[i:i+block_size]
        ciphertext += encrypt_block(block, key_matrix)
    
    return ciphertext

def get_key_matrix(matrix_size):
    print(f"\nEnter the key matrix of size {matrix_size}x{matrix_size}:")
    key_matrix = []
    for i in range(matrix_size):
        row = list(map(int, input(f"Enter row {i+1} values separated by space: ").split()))
        key_matrix.append(row)
    return np.array(key_matrix)

def main():
    matrix_size = int(input("Enter the size of the key matrix: "))
    key_matrix = get_key_matrix(matrix_size)

    plaintext = input("Enter the plaintext: ").upper().replace(" ", "")
    print(f"\nOriginal plaintext: {plaintext}")

    ciphertext = hill_cipher_encrypt(plaintext, key_matrix)
    print(f"\nEncrypted text: {ciphertext}\n")

if __name__ == "__main__":
    main()
