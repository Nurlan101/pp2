def numb(n):
    b = n
    while b > 0:
        yield b
        b -= 1

n = int(input())

for i in numb(n):
    print(i)