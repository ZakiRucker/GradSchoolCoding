'''
4. Define a function input_positive that prompts the user to enter a positive integer. If the
number is positive, return this number. If not, prompt the user again (the input was 0 or
negative). Repeat the prompt until a positive integer is entered. Use this function to input
two positive numbers and compute the sum of all integers between them using the get_total
function. Note that the get_total function requires the first parameter to be the smaller of the
two parameters.
'''
def input_positive():
    while True:
        val = int(input("Enter positive integer: "))
        if val > 0: return val
        print("Invalid entry")

num1 = input_positive()
num2 = input_positive()

def get_total(low, high):
    ## assume exclusive for 'between'
    sum = 0

    for i in range(low + 1, high):
        sum += i

    return sum


low, high = (num1, num2) if num1 < num2 else (num2, num1)
# low, hihg = min(num1, num2), max(num1, num2)
print(get_total(low, high))
