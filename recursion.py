def sum_to_n(n):
    if n == 1:
        return 1
    else:
        return n + sum_to_n(n - 1)
    
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) +  fibonacci(n - 2)
    

def fibonacci1(n):
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b
    
counter = 0

def fibonacci2(n):
    global counter
    counter += 1
    if n <= 1:
        return n
    return fibonacci2(n - 1) + fibonacci2(n - 2)

print(fibonacci2(5))
print(f"Всего вызовов: {counter}")  # удивишься результату!
print(sum_to_n(5))
print(fibonacci(8))
print(fibonacci1(8))
print(fibonacci2(8))
    