import fibonacci

def fibonacci(limit):
    fibonacci_numbers = []
    a, b = 0, 1
    
    for _ in range(limit):
        fibonacci_numbers.append(a)
        a, b = b, a + b
        
    return fibonacci_numbers
