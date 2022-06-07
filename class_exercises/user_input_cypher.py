import string

word = input("Enter a word to encode: ")
while not word.isalpha():
    word = input("Enter a word to encode: ")
print(word)

key = input("Enter a digit for the word: ")
while not key.isdigit():
    key = input("Enter a digit for the word: ")
print(key)
print()
alpha = string.ascii_lowercase
spill = alpha[int(key):] + alpha[: int(key)]
cipher = word.translate(str.maketrans(alpha, spill))
print(cipher)
print(cipher.translate(str.maketrans(spill, alpha)))
