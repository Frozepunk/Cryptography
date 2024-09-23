import string

def generate_matrix(keyword):
    matrix = [[' ' for _ in range(5)] for _ in range(5)]
    keyword = keyword.upper()
    keyword_chars = []
    seen = set()
    
    for char in keyword:
        if char not in seen and char != 'J':
            keyword_chars.append(char)
            seen.add(char)
    
    random_chars = [char for char in string.ascii_uppercase if char not in keyword_chars and char != 'J']
    random_chars.sort()

    index = 0
    for i in range(5):
        for j in range(5):
            if index < len(keyword_chars):
                matrix[i][j] = keyword_chars[index]
                index += 1
            else:
                matrix[i][j] = random_chars.pop(0)

    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(row))

def prepare_text(text):
    text = text.upper().replace(' ', '')
    result = []
    i = 0
    while i < len(text):
        if i + 1 < len(text) and text[i] != text[i + 1]:
            result.append(text[i:i + 2])
            i += 2
        else:
            result.append(text[i] + 'X')
            i += 1
    return result

def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char or (char == 'I' and matrix[i][j] == 'J') or (char == 'J' and matrix[i][j] == 'I'):
                return (i, j)

def encrypt(matrix, text):
    result = []
    for pair in text:
        pos1 = find_position(matrix, pair[0])
        pos2 = find_position(matrix, pair[1])
        if pos1[0] == pos2[0]:  
            result.append(matrix[pos1[0]][(pos1[1] + 1) % 5] + matrix[pos2[0]][(pos2[1] + 1) % 5])
        elif pos1[1] == pos2[1]:  
            result.append(matrix[(pos1[0] + 1) % 5][pos1[1]] + matrix[(pos2[0] + 1) % 5][pos2[1]])
        else:  
            result.append(matrix[pos1[0]][pos2[1]] + matrix[pos2[0]][pos1[1]])
    return ' '.join(result)

def decrypt(matrix, text, original_text):
    result = []
    original_text = original_text.upper().replace(' ', '')  # Remove spaces for comparison
    
    for idx, pair in enumerate(text.split()):
        pos1 = find_position(matrix, pair[0])
        pos2 = find_position(matrix, pair[1])
        
        if pos1[0] == pos2[0]:  
            decrypted_pair = matrix[pos1[0]][(pos1[1] - 1) % 5] + matrix[pos2[0]][(pos2[1] - 1) % 5]
        elif pos1[1] == pos2[1]:  
            decrypted_pair = matrix[(pos1[0] - 1) % 5][pos1[1]] + matrix[(pos2[0] - 1) % 5][pos2[1]]
        else:  
            decrypted_pair = matrix[pos1[0]][pos2[1]] + matrix[pos2[0]][pos1[1]]
        
        # Check the original plain text for 'I' or 'J' and adjust the decrypted text accordingly
        for i in range(2):
            if original_text[idx * 2 + i] == 'I' and decrypted_pair[i] == 'J':
                decrypted_pair = decrypted_pair[:i] + 'I' + decrypted_pair[i + 1:]
            elif original_text[idx * 2 + i] == 'J' and decrypted_pair[i] == 'I':
                decrypted_pair = decrypted_pair[:i] + 'J' + decrypted_pair[i + 1:]
        
        result.append(decrypted_pair)
    
    return ''.join(result)

def main():
    text = input("Enter the plain text: ")
    keyword = input("Enter the keyword: ")
    matrix = generate_matrix(keyword)
    print("\nMatrix:")
    print_matrix(matrix)
    
    prepared_text = prepare_text(text)
    print("Prepared text:", ' '.join(prepared_text))
    
    encrypted_text = encrypt(matrix, prepared_text)
    print("\nEncrypted text:", encrypted_text)

    decrypted_text = decrypt(matrix, encrypted_text, text)  # Pass original text
    print("\nDecrypted text:", decrypted_text)

if __name__ == "__main__":
    main()