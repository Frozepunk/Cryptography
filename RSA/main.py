import math
from sympy import mod_inverse

def text_to_numbers(text):
    return [ord(char) - ord('a') for char in text.lower() if 'a' <= char <= 'z']

def numbers_to_text(numbers):
    return ''.join(chr(num + ord('a')) for num in numbers)

p = int(input("Enter the value of p (prime number): "))
q = int(input("Enter the value of q (prime number): "))
n = p * q
phi = (p - 1) * (q - 1)
print("n =", n)
print("phi(n) =", phi)

e = int(input("Enter the value of e (1 < e < phi(n)): "))
while e >= phi or math.gcd(e, phi) != 1:
    print("Invalid e. Ensure 1 < e < phi(n) and gcd(e, phi) = 1.")
    e = int(input("Enter a valid value for e: "))
print("e =", e)

d = mod_inverse(e, phi)
print("d =", d)

print(f'Public key: ({e}, {n})')
print(f'Private key: ({d}, {n})')

text = input("Enter a text to encrypt (only alphabets): ")
numbers = text_to_numbers(text)
print("Numerical representation of text:", numbers)

encrypted_numbers = [pow(num, e, n) for num in numbers]
print("Encrypted numerical values:", encrypted_numbers)

decrypted_numbers = [pow(num, d, n) for num in encrypted_numbers]
print("Decrypted numerical values:", decrypted_numbers)

decrypted_text = numbers_to_text(decrypted_numbers)
print("Decrypted text:", decrypted_text)