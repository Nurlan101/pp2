#1
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#3
for x in range (6):
  print(x)

#4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break 
  print(x)