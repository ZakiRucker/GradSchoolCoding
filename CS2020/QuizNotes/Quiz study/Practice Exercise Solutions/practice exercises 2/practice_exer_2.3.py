'''
3. Define a function get_total that returns the sum of integers between the two parameters low
and high. Assume low is less than or equal to high. Use this function to compute the sum of
integers between 10 and 100.
'''
def get_total(low, high):
    ## assume exclusive for 'between'
    sum = 0

    for i in range(low + 1, high):
        sum += i

    return sum

print(get_total(10, 100))

