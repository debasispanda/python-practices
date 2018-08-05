def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(2000)


def calculate(val1, val2, operation):
    """calculator."""
    return {
        'add'       : val1 + val2,
        'substract' : val1 - val2,
        'multiply'  : val1 * val2,
        'divide'    : val1 / val2    
    }[operation]

sum = calculate(10, 20, 'add')
print("10 + 20 = " + str(sum))

result = calculate(10, 20, 'multiply')
print('10 x 20 = ' + str(result))