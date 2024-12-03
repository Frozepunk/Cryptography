from sympy import gcd, mod_inverse
plain_text = input("Enter the plain text: ")
p = int(input("Enter a prime number p: "))
q = int(input("Enter a prime number q: "))
plain_text_nums = [ord(char) for char in plain_text]
print(f"\nPlain Text (as numbers): {plain_text_nums}")
n = p * q
euler_n = (p - 1) * (q - 1)
print(f"\nValue of n (p * q) = {n}")
print(f"Euler's function ϕ(n) = (p-1)(q-1) = {euler_n}")
print("\nSelecting e such that 1 < e < ϕ(n) and gcd(e, ϕ(n)) = 1...")
for e in range(2, euler_n):
    if gcd(euler_n, e) == 1:
        break
    
print(f"Selected e = {e}")
d = mod_inverse(e, euler_n)
print(f"Calculated d (modular inverse of e mod ϕ(n)) = {d}")
print(f"\nPublic Key (PU) = ({e}, {n})")
print(f"Private Key (PR) = ({d}, {n})")
cipher_text_nums = [pow(num, e, n) for num in plain_text_nums]
print(f"\nCiphertext (C) = {cipher_text_nums}")
decrypted_text_nums = [pow(c, d, n) for c in cipher_text_nums]
decrypted_text = ''.join(chr(num) for num in decrypted_text_nums)
print(f"Decrypted Plain Text (M) = {decrypted_text}")