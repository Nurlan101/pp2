def enum(n):
    b = 1
    while b < n:
        yield b * 2
        b += 1

n = int(input())

for i in enum(n // 2):
    print(i)