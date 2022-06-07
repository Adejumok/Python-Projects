import string

s = 'hello'
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())

t = ' O babee '
print(t.strip())
print(t.rstrip())
print(t.lstrip())
print(t.find('a'))
print(t.rfind('a'))
print(t.find('g'))
print(s.rfind('o'))
print(s.find('e'))

print(s.find("h", 0))
print(t.isalpha())
print(s.removesuffix("o"))
print(s.swapcase())
print(t.split())
print(s.replace("h", "o", 1))

f = "10110110"
print(f.replace("0", "1", 3))
print(f.translate(str.maketrans("01", "10")))
print(string.digits)
print(string.ascii_letters)

