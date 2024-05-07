def factorial_iterative (n):
    "Calculate factorial of a positive integer using iteration."

    if n < 0 :
        print("Factorial is defined only for non-negative integers")
    result = 1 
    for i in range (1, n+1):
        result *= i
    return result

def factorial_recursion(n):
        "Calculate factorial of a positive integer using iteration."
        if n < 0 :
            print("Factorial is defined only for non-negative integers")
        if n == 0:
            return 1
        return n * factorial_recursion(n-1)

def clumsy(n):
    if n < 0:
        raise ValueError("Clumsy factorial is defined only for non-negative integers")
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 6
    
    result = n * (n - 1) // (n - 2) + (n - 3)  
    n -= 4
    
    while n >= 4:
        result -= (n * (n - 1)) // (n - 2)       
        result += (n - 3)                      
        n -= 4                                  
    return result - clumsy(n)