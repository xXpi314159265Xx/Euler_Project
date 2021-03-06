# Project Euler
# Problem 2

# Each new term in the Fibonocci sequence is generated by adding the previous
# two terms. By starting with 1 and 2, the first 10 terms will be:
# 1,2,3,5,8,13,21,34,55,89,...

# By considering the terms in the Fibonacci sequence whose values do not exceed
# four million, find the sum of the even-valued terms.

# Generate all even Fibonacci sequence values < 4,000,000 in a list and return
# the sum of the values

def fibonacci(max):
    '''Generates a list of even Fibonacci numbers less than max and return the sum of those numbers.'''

    fib_list = []
    num_1 = 1
    num_2 = 1
    while num_1 < max:
        new_num = num_1 + num_2
        if new_num % 2 == 0:
            fib_list.append(new_num)
        num_2 = num_1
        num_1 = new_num
    return sum(fib_list)

print(fibonacci(4000000))
