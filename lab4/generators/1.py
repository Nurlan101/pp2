n = int(input())

v = (i * i for i in range(1, n))

print(v)
for i in v:
    print(i)