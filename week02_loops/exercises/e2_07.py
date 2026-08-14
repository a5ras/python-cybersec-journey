"""
Prime checker Determine whether a number is prime, efficiently. Hint: you only
need to test divisors up to the square root. Expected: 97 → prime · 91 → not prime
"""
def prime_checker(number):
    # for i in range(2,number):
    #     if number % i == 0:
    #         return "not prime"
    # return "prime"
    i = 2
    while i * i <= number:
        if number % i == 0:
            return "not prime"
        i+=1
    return "prime"
x = prime_checker(4)
print(x)