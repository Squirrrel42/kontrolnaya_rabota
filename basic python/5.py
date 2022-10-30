# задача 5 tasks.pdf

n = int(input())
m = n

prime = [0] * n
p = 2

if(n == 0):
    print(0)
elif(n == 1 or n == -1):
    print(1)
else:
    while (m > 1):
        if (m % p == 0):
            prime[p] += 1
            m = m / p
        else:
            p += 1

    print(max(prime))