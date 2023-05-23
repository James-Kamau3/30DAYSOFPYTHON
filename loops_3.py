# Fibonacci: Write a program that prompts the user to enter a positive integer n, 
# and then prints the first n Fibonacci numbers. The Fibonacci sequence starts with 
# 0 and 1, and each subsequent number is the sum of the two preceding numbers.

n = int(input('Enter range: '))

def fibonacci(n):
    seq = [0, 1]
    
    for i in range(2, n):
        next_no = seq[i-1] + seq[i-2]
        seq.append(next_no)
    return seq
                      
print(f"Fibonacci sequence up to {n} numbers:")
fib = fibonacci(n)
print(fib)

    
