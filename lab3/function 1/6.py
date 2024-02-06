def rev(x):
    x.reverse()

sent = input().split() # splits the string into a list words
rev(sent)
for i in sent:
    print(i, end = ' ') 