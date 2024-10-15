import numpy as np

def letter_to_num(letter):
    return ord(letter.upper()) - ord('A')

def num_to_letter(num):
    return chr((num % 26) + ord('A'))

def encrypt_block(plain_block, key_matrix):
    print(f"\nEncrypting block: {plain_block}")
    plain_numbers = [letter_to_num(c) for c in plain_block]
    print(f"Corresponding numbers for block '{plain_block}': {plain_numbers}")

    # Convert the plaintext block into a column vector
    plain_vector = np.array(plain_numbers).reshape(-1, 1)
    print(f"\nPlaintext matrix (column vector):\n{plain_vector}\n")
    
    print(f"Key matrix:\n{key_matrix}\n")
    
    # Perform the matrix multiplication
    result = np.dot(key_matrix, plain_vector) % 26
    print(f"Matrix multiplication result (mod 26):\n{result}")      

    encrypted_block = ''.join([num_to_letter(num[0]) for num in result])
    print(f"Encrypted block: {encrypted_block}")
    
    return encrypted_block

def decrypt_block(cipher_block, inverse_key_matrix):
    print(f"\nDecrypting block: {cipher_block}")
    cipher_numbers = [letter_to_num(c) for c in cipher_block]
    print(f"Corresponding numbers for block '{cipher_block}': {cipher_numbers}")

    # Convert the ciphertext block into a column vector
    cipher_vector = np.array(cipher_numbers).reshape(-1, 1)
    print(f"\nCiphertext matrix (column vector):\n{cipher_vector}\n")
    
    print(f"Inverse key matrix:\n{inverse_key_matrix}\n")
    
    # Perform the matrix multiplication
    result = np.dot(inverse_key_matrix, cipher_vector) % 26
    print(f"Matrix multiplication result (mod 26):\n{result}")

    decrypted_block = ''.join([num_to_letter(num[0]) for num in result])
    print(f"Decrypted block: {decrypted_block}")
    
    return decrypted_block

def hill_cipher_encrypt(plaintext, key_matrix):
    block_size = key_matrix.shape[0]
    
    if len(plaintext) % block_size != 0:
        plaintext += 'X' * (block_size - len(plaintext) % block_size)
    print(f"\nPadded plaintext: {plaintext}")

    ciphertext = ''
    for i in range(0, len(plaintext), block_size):
        block = plaintext[i:i + block_size]
        ciphertext += encrypt_block(block, key_matrix)
    
    return ciphertext

def hill_cipher_decrypt(ciphertext, inverse_key_matrix):
    block_size = inverse_key_matrix.shape[0]

    plaintext = ''
    for i in range(0, len(ciphertext), block_size):
        block = ciphertext[i:i + block_size]
        plaintext += decrypt_block(block, inverse_key_matrix)

    return plaintext

def get_key_matrix(matrix_size):
    print(f"\nEnter the key matrix of size {matrix_size}x{matrix_size}:")
    key_matrix = []
    for i in range(matrix_size):
        row = list(map(int, input(f"Enter row {i + 1} values separated by space: ").split()))
        key_matrix.append(row)
    return np.array(key_matrix)

def mod_inverse(matrix, mod):
    # Calculate determinant
    det = int(np.round(np.linalg.det(matrix)))  # Round to avoid floating point issues
    det_inv = pow(det, -1, mod)  # Modular inverse of the determinant

    # Calculate the adjugate (transpose of cofactor matrix)
    adjugate = np.round(det * np.linalg.inv(matrix)).astype(int) % mod

    # Multiply the adjugate matrix by the modular inverse of the determinant
    inverse_matrix = (det_inv * adjugate) % mod

    return inverse_matrix

def main():
    matrix_size = int(input("Enter the size of the key matrix: "))
    key_matrix = get_key_matrix(matrix_size)

    plaintext = input("Enter the plaintext: ").upper().replace(" ", "")
    print(f"\nOriginal plaintext: {plaintext}")

    ciphertext = hill_cipher_encrypt(plaintext, key_matrix)
    print(f"\nEncrypted text: {ciphertext}\n")

    # Decryption
    inverse_key_matrix = mod_inverse(key_matrix, 26)
    print(f"\nInverse key matrix (mod 26):\n{inverse_key_matrix}\n")

    decrypted_text = hill_cipher_decrypt(ciphertext, inverse_key_matrix)
    print(f"\nDecrypted text: {decrypted_text}\n")

if __name__ == "__main__":
    main()
