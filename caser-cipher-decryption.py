result = []
text = input("Enter text\n ")
key = int(input("Enter the key value \n"))
for char in text:
    if char.islower():
        base = ord('a')
        res = chr((ord(char) - base - key) % 26 + base)
        result.append(res)
    elif char.isupper():
        base = ord('A')
        res = chr((ord(char) - base - key) % 26 + base)
        result.append(res)
    elif char.isdigit():
        base = ord('0')
        res = chr((ord(char) - base - key) % 10 + base)
        result.append(res)
    else:
        result.append(char)
print(''.join(result))
# def caeser_cipher():
#     result = []
#     text = input("Enter text\n ")
#     key = int(input("Enter the key value \n"))
#     for char in text:
#         if char.islower():
#             base = ord('a')
#             res = chr((ord(char) - base - key) % 26 + base)
#             result.append(res)
#         elif char.isupper():
#             base = ord('A')
#             res = chr((ord(char) - base - key) % 26 + base)
#             result.append(res)
#         elif char.isdigit():
#             base = ord('0')
#             res = chr((ord(char) - base - key) % 10 + base)
#             result.append(res)
#         else:
#             result.append(char)
#     print(''.join(result))