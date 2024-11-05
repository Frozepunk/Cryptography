import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

def rail_fence_encrypt(plaintext, key):
    fence = [[] for _ in range(key)]
    rail = 0
    var = 1

    for char in plaintext:
        fence[rail].append(char)
        rail += var
        if rail == key - 1 or rail == 0:
            var = -var

    # Create a graph visualization of the Rail Fence
    plot_rail_fence(fence, key)

    encrypted_text = ''.join(''.join(row) for row in fence)
    return encrypted_text

def rail_fence_decrypt(ciphertext, key):
    fence = [['' for _ in range(len(ciphertext))] for _ in range(key)]
    rail = 0
    var = 1
    for i in range(len(ciphertext)):
        fence[rail][i] = '*'
        rail += var
        if rail == key - 1 or rail == 0:
            var = -var

    index = 0
    for row in range(key):
        for col in range(len(ciphertext)):
            if fence[row][col] == '*' and index < len(ciphertext):
                fence[row][col] = ciphertext[index]
                index += 1

    decrypted_text = []
    rail = 0
    var = 1
    for i in range(len(ciphertext)):
        decrypted_text.append(fence[rail][i])
        rail += var
        if rail == key - 1 or rail == 0:
            var = -var

    return ''.join(decrypted_text)

def plot_rail_fence(fence, key):
    # Prepare for plotting
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.set_xlim(-0.5, len(fence[0]) - 0.5)
    ax.set_ylim(key - 0.5, -0.5)

    for i in range(key):
        ax.text(-0.5, i, f"Rail {i}", ha='right', va='center', fontsize=10)

    for i in range(len(fence[0])):
        for j in range(key):
            if i < len(fence[j]):
                ax.text(i, j, fence[j][i], ha='center', va='center', fontsize=12, color='blue')

    ax.axis('off')
    plt.show()

def on_encrypt():
    plaintext = entry_plaintext.get()
    try:
        key = int(entry_key.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Key must be an integer.")
        return

    if key <= 1:
        messagebox.showerror("Invalid Input", "Key must be greater than 1.")
        return

    encrypted = rail_fence_encrypt(plaintext, key)
    entry_encrypted.delete(0, tk.END)
    entry_encrypted.insert(0, encrypted)

    decrypted = rail_fence_decrypt(encrypted, key)
    entry_decrypted.delete(0, tk.END)
    entry_decrypted.insert(0, decrypted)

# GUI setup
root = tk.Tk()
root.title("Rail Fence Cipher")

# Plaintext input
tk.Label(root, text="Enter Plaintext:").grid(row=0, column=0, padx=10, pady=5)
entry_plaintext = tk.Entry(root, width=40)
entry_plaintext.grid(row=0, column=1, padx=10, pady=5)

# Key input
tk.Label(root, text="Enter Key (number of rails):").grid(row=1, column=0, padx=10, pady=5)
entry_key = tk.Entry(root, width=40)
entry_key.grid(row=1, column=1, padx=10, pady=5)

# Encrypted text
tk.Label(root, text="Encrypted Text:").grid(row=2, column=0, padx=10, pady=5)
entry_encrypted = tk.Entry(root, width=40)
entry_encrypted.grid(row=2, column=1, padx=10, pady=5)

# Decrypted text
tk.Label(root, text="Decrypted Text:").grid(row=3, column=0, padx=10, pady=5)
entry_decrypted = tk.Entry(root, width=40)
entry_decrypted.grid(row=3, column=1, padx=10, pady=5)

# Encrypt button
btn_encrypt = tk.Button(root, text="Encrypt and Decrypt", command=on_encrypt)
btn_encrypt.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()

