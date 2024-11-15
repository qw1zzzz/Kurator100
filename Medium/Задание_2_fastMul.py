import sys
sys.set_int_max_str_digits(1000000)
def power(a, n):
    return (1 if n == 0
            else power(a * a, n // 2) if n % 2 == 0
            else a * power(a, n - 1))
x = int(input("Введите основание:"))
y = int(input("Введите степень"))
print(power(x, y))