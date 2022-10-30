#задача 4 из tasks.pdf

n = int(input())

numbers = []

if(n < 0):
    c = -1
    n = -n
else:
    c = 1

while(n > 0):
    numbers.append(n % 10)
    n = n // 10

numbers.sort(reverse=True)

while(numbers[-1] == 0):
    i = len(numbers) - 2
    while(numbers[i] == 0):
        i -= 1

    numbers[-1] = numbers[i]
    numbers[i] = 0

res = 0

for i in range(len(numbers)):
    res += numbers[i] * 10 ** i
res = res * c

print(res)