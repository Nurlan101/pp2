def numb(s,e):
    for i in range(s,e):
        yield i * i

s = int(input())
e = int(input())

for i in numb(s,e):
    print(i)