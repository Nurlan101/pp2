def numb(n):
    b = 1
    while b < n:
        if(b % 3 == 0 or b % 4 == 0):
            yield b
            b += 1
        else:
            b += 1

n = int(input())

for i in numb(n):
    print(i)