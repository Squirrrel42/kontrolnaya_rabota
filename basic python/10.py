#задача 10 из tasks.pdf

f = open('input.txt', 'r')
text = f.read()
f.close()

text = text.lower()
text = ''.join(c for c in text if c.isalpha())

alphabet = [0] * 26

for c in text:
    number = ord(c) - 97
    if(number >= 0 and number < 26):
        alphabet[number] += 1

for i in range(len(alphabet)):
    print(chr(i + 97),':', alphabet[i])