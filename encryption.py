import random
import string
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)

#ENCRYPT
text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"The original text is {text}")
print(f"This is the encrypted text {cipher_text}")

#DECRYPT
cipher_text = input("Enter a message to encrypt: ")
text = ""

for letter in cipher_text:
    index = key.index(letter)
    text += chars[index]

print(f"This is the encrypted text {cipher_text}")
print(f"This is the decryped text {text} ")