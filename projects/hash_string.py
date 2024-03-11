import hashlib
def compare(string1, string2, shift):
    hashed1 = hashlib.sha256(caesar_cipher(string1, shift).encode()).hexdigest()
    hashed2 = hashlib.sha256(caesar_cipher(string2, shift).encode()).hexdigest()
    return hashed1 == hashed2
def caesar_cipher(string, shift):
    encrypted_string = ""
    for char in string:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_string += encrypted_char
        else:
            encrypted_string += char
    return encrypted_string
first = input("Введите строку: ")
second = input("Введите строку: ")
shift = int(input("Введите сдвиг: "))
if compare(first, second, shift):
    print("Строки совпадают")
else:
    print("Строки не совпадают")
