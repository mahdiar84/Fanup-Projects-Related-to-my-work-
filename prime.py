import math
# we use try because if we give an string we don't face an Error, we'll face a Warning!
try:
    n = int(input("Enter a num: "))
    # Define a prime func
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.pow(n, 0.5)) + 1):
            if n % i == 0:
                return False
        
        return True
   
except ValueError:
    print("Only integers")
else:
    print(is_prime(n))