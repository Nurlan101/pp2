def is_prime(n):
    if n <= 1:
        return False  
    for i in range(2, n):
        if n % i == 0:
            return False  
    return True  

num = int(input())
if is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
