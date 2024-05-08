#factorial_iterative

def factorial_iterative (n):
    """
    Calculate factorial of a positive integer using iteration.
    
    Arguments:
        n (int): The integer for which factorial is to be calculated.
        
    Returns:
        int: Factorial of the given integer.
        
    Raises:
        ValueError: If the input is negative.
    """

    if n < 0 :
        print("Factorial is defined only for non-negative integers")
    result = 1 
    for i in range (1, n+1):
        result *= i
    return result

#factorial_recursion

def factorial_recursion(n):
        """
        Calculate factorial of a positive integer using recursion.
    
        Arguments:
            n (int): The integer for which factorial is to be calculated.
        
        Returns:
            int: Factorial of the given integer.
        
        Raises:
            ValueError: If the input is negative.
    
        """

        if n < 0 :
            print("Factorial is defined only for non-negative integers")
        if n == 0:
            return 1
        return n * factorial_recursion(n-1)

#clumsy

def clumsy(n: int) -> int:
        """
        Calculate the clumsy factorial of a non-negative integer.

        Clumsy factorial is a variant of factorial calculation where 
        multiplication operations are swapped with a fixed rotation of operations
        (multiply *, divide /, add +, and subtract -) in this order.
    
        Arguments:
            n (int): The non-negative integer for which clumsy factorial is to be calculated.
        
        Returns:
            int: Clumsy factorial of the given integer.
        
        Raises:
            ValueError: If the input is negative.
        """
        
        if n < 0:
            print("Clumsy factorial is defined only for non-negative integers")
            return None
        
        if n == 1:
            return 1
        
        stack = [n]
        operation_index  = 0 
        
        for i in range(n-1, 0, -1):
            if operation_index  % 4 == 0: # Multiply operation
                stack[-1] *= i 
            elif operation_index  % 4 == 1: # Divide operation
                stack[-1] = int(stack[-1] / i)
            elif operation_index  % 4 == 2: # Addition operation
                stack.append(i)
            elif operation_index  % 4 == 3: # Subtraction operation
                stack.append(-i)
            
            operation_index  += 1
        
        return sum(stack)