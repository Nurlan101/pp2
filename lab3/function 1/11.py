def palindrome(s):
    s2 = s[::-1]  #checks reversed string is equal to the 1st string
    if s2 == s:
        print("This word is palindrome")
    else:
        print("Not palindrome")
s = input()
palindrome(s)