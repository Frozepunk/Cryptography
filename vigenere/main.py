def generate_key(message, key):
    # Convert key to a list
    key = list(key)
    
    # If key length matches message length, return it
    if len(message) == len(key):
        return "".join(key)
    
    # Extend the key to match the length of the message
    for i in range(len(message) - len(key)):
        key.append(key[i % len(key)])
    
    return "".join(key)

def char_to_num(char):
    """Convert a character to its corresponding numerical value (A=0, B=1, ..., Z=25)."""
    return ord(char.upper()) - ord('A')

def num_to_char(num):
    """Convert a numerical value back to its corresponding character."""
    return chr(num + ord('A'))

def encrypt(message, key):
    encrypted_message = []
    print(f"Encrypting message: '{message}' with key: '{key}'")
    
    # Convert characters to numerical values
    message_nums = [char_to_num(c) for c in message if c.isalpha()]
    key_nums = [char_to_num(k) for k in key]
    
    print(f"Message as numbers: {message_nums}")
    print(f"Key as numbers: {key_nums}")
    
    # Encrypt each character
    for i, char in enumerate(message):
        if char.isalpha():
            shift = (char_to_num(char) + char_to_num(key[i])) % 26
            encrypted_char = num_to_char(shift)
            encrypted_message.append(encrypted_char)
            print(f"Step {i + 1}: '{char}' + '{key[i]}' -> '{encrypted_char}' (Shift: {shift})")
        else:
            encrypted_message.append(char)
            print(f"Step {i + 1}: Non-alphabet character '{char}' remains unchanged.")
    
    return "".join(encrypted_message)

def decrypt(encrypted_message, key):
    decrypted_message = []
    print(f"\nDecrypting message: '{encrypted_message}' with key: '{key}'")
    
    # Convert encrypted characters to numerical values
    encrypted_nums = [char_to_num(c) for c in encrypted_message if c.isalpha()]
    key_nums = [char_to_num(k) for k in key]
    
    print(f"Encrypted message as numbers: {encrypted_nums}")
    print(f"Key as numbers: {key_nums}")
    
    # Decrypt each character
    for i, char in enumerate(encrypted_message):
        if char.isalpha():
            shift = (char_to_num(char) - char_to_num(key[i]) + 26) % 26
            decrypted_char = num_to_char(shift)
            decrypted_message.append(decrypted_char)
            print(f"Step {i + 1}: '{char}' - '{key[i]}' -> '{decrypted_char}' (Shift: {shift})")
        else:
            decrypted_message.append(char)
            print(f"Step {i + 1}: Non-alphabet character '{char}' remains unchanged.")
    
    return "".join(decrypted_message)

def main():
    # Get user input for message and key
    message = input("Enter the message to encrypt: ")
    key = input("Enter the key: ")
    
    # Generate a full key that matches the message length
    full_key = generate_key(message, key)
    
    # Encrypt the message
    encrypted_message = encrypt(message, full_key)
    
    # Decrypt the message
    decrypted_message = decrypt(encrypted_message, full_key)
    
    # Output final results
    print(f"\nFinal Encrypted Message: '{encrypted_message}'")
    print(f"Decrypted Message: '{decrypted_message}'")

if __name__ == "__main__":
    main()
