#Simple Factoral Program

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(raw_input("Please type a positive number to compute the factorial: "))
print(factorial(n))

