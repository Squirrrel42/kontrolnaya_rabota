#задача 3 из task_template

date = str(input())

date = date.split(sep='.')
for i in range(3):
    date[i] = int(date[i])

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if(date[0]%4 == 0 and date[1] == 2 and date[3] == 29):
    print(True)
else:
    if(date[1] > 0 and date[1] <= 12):
        if(date[2] > 0 and date[2] <= months[date[1]-1]):
            print(True)
        else:
            print(False)
    else:
        print(False)