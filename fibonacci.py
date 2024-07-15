from fibonacci import fibonacci

def main():
    try:
        limit = int(input("Enter the number of Fibonacci terms: "))
        fibonacci_numbers = fibonacci(limit)
        
        print(f"Fibonacci sequence {limit}:")
        print(', '.join(map(str, fibonacci_numbers)))
        
    except Exception:
        print("wrong input!")
    
if __name__ == "__main__":
    main()
