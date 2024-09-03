# Cryptography

## Caeser Cipher
Imagine you have a **secret message**, and you want to hide it so only certain people can read it. One simple way to do this is using a **Caesar cipher**. Here's how it works:

## 1. Shift the Alphabet

Choose a number to shift each letter in the alphabet. For example, if you choose a shift of **3**, then:
- 'A' becomes 'D'
- 'B' becomes 'E'
- and so on.

## 2. Encode the Message

Write your message using the shifted alphabet. For example, if your message is **"HELLO"** and your shift is **3**, you would encode it as **"KHOOR"**.

## 3. Decode the Message

To read the message, the person needs to know the shift number. They then reverse the process, shifting letters back to the original alphabet.

## Source code 


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
