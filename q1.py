def getPrimeNumbers(n):
    def isPrime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    # using comprehension to generate list
    prime_numbers = [num for num in range(2, n + 1) if isPrime(num)]
    return prime_numbers

n = 20
result = getPrimeNumbers(n)
print(f"Prime numbers between 2 and {n}: {result}")
