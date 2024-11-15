import sys
sys.set_int_max_str_digits(125000)

def factorial(n):
    if (n <= 1):
        return 1
    else:
        return (n * factorial(n-1))
    
n = int(input("Введите число:"))

def power(a, n):
    return (1 if n == 0
            else power(a * a, n // 2) if n % 2 == 0
            else a * power(a, n - 1))

x = int(factorial(n))
y = n
print(power(x, y))


