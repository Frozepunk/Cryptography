# Cryptography
## ceasar cipher

```def caesar_cipher():
    text = input("Enter text: ")
    key = int(input("Enter the key value: "))

    # Encryption
    encrypted = []
    for char in text:
        if char.islower():
            base = ord('a')
            res = chr((ord(char) - base + key) % 26 + base)
            encrypted.append(res)
        elif char.isupper():
            base = ord('A')
            res = chr((ord(char) - base + key) % 26 + base)
            encrypted.append(res)
        elif char.isdigit():
            base = ord('0')
            res = chr((ord(char) - base + key) % 10 + base)
            encrypted.append(res)
        else:
            encrypted.append(char)

    encrypted_text = ''.join(encrypted)
    print("Encrypted text-->", encrypted_text)

    # Decryption
    decrypted = []
    for char in encrypted_text:
        if char.islower():
            base = ord('a')
            res = chr((ord(char) - base - key) % 26 + base)
            decrypted.append(res)
        elif char.isupper():
            base = ord('A')
            res = chr((ord(char) - base - key) % 26 + base)
            decrypted.append(res)
        elif char.isdigit():
            base = ord('0')
            res = chr((ord(char) - base - key) % 10 + base)
            decrypted.append(res)
        else:
            decrypted.append(char)

    print("Decrypted text-->", ''.join(decrypted))

caesar_cipher()
```