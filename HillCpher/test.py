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

def get_key_matrix(matrix_size):
    print(f"\nEnter the key matrix of size {matrix_size}x{matrix_size}:")
    key_matrix = []
    for i in range(matrix_size):
        row = list(map(int, input(f"Enter row {i + 1} values separated by space: ").split()))
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
