def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):  #iterates through numbers from 2 to the square root of the given number 
        if n % i == 0:
            return False
    return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print(prime_numbers) 
