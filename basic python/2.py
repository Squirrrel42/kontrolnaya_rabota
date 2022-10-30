#задача 2 из tasks.pdf

ы = str(input())

ы = ы.lower()

ы = ''.join(c for c in ы if c.isalpha() == True)

for i in range(int(len(ы)/2)):
    c = 1
    if(ы[i] != ы[len(ы) - 1 - i]):
        c = 0
        break

if(c == 1):
    print(True)
else:
    print(False)