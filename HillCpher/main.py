import numpy as np

def mod_inverse(a, m):
    """Return the modular inverse of a under modulo m."""
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def create_key_matrix(key):
    """Create a 2x2 key matrix from the key string."""
    key_matrix = np.array([[ord(key[0]) - ord('A'), ord(key[1]) - ord('A')],
                            [ord(key[2]) - ord('A'), ord(key[3]) - ord('A')]])
    return key_matrix

def encrypt(plaintext, key):
    """Encrypt the plaintext using the Hill cipher."""
    key_matrix = create_key_matrix(key)
    plaintext = plaintext.upper().replace(" ", "")
    
    # Padding the plaintext if necessary
    while len(plaintext) % 2 != 0:
        plaintext += 'X'  # Padding with 'X'

    ciphertext = ''
    
    for i in range(0, len(plaintext), 2):
        # Create a vector from the plaintext characters
        vector = np.array([[ord(plaintext[i]) - ord('A')],
                           [ord(plaintext[i+1]) - ord('A')]])

        # Encrypt the vector
        encrypted_vector = np.dot(key_matrix, vector) % 26
        
        # Convert back to characters
        ciphertext += chr(encrypted_vector[0][0] + ord('A'))
        ciphertext += chr(encrypted_vector[1][0] + ord('A'))
    
    return ciphertext

def decrypt(ciphertext, key):
    """Decrypt the ciphertext using the Hill cipher."""
    key_matrix = create_key_matrix(key)
    det = int(np.round(np.linalg.det(key_matrix))) % 26
    
    # Find the modular inverse of the determinant
    det_inv = mod_inverse(det, 26)
    
    # Find the adjugate matrix
    adjugate_matrix = np.array([[key_matrix[1][1], -key_matrix[0][1]],
                                 [-key_matrix[1][0], key_matrix[0][0]]]) % 26
    inverse_key_matrix = (det_inv * adjugate_matrix) % 26
    
    # Prepare to decrypt
    ciphertext = ciphertext.upper().replace(" ", "")
    plaintext = ''
    
    for i in range(0, len(ciphertext), 2):
        vector = np.array([[ord(ciphertext[i]) - ord('A')],
                           [ord(ciphertext[i+1]) - ord('A')]])
        
        decrypted_vector = np.dot(inverse_key_matrix, vector) % 26
        
        plaintext += chr(decrypted_vector[0][0] + ord('A'))
        plaintext += chr(decrypted_vector[1][0] + ord('A'))
    
    return plaintext.replace('X', '')  # Remove padding

# Example usage
key = "HILL"  # 2x2 key matrix
plaintext = "HELLO"
ciphertext = encrypt(plaintext, key)
decrypted_text = decrypt(ciphertext, key)

print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted: {decrypted_text}")
