def addition(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def divide(num1, num2):
    return num1 / num2


def multiply(num1, num2):
    return num1 * num2


def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


def fibbonacci(num):
    # first two terms
    n1, n2 = 0, 1
    count = 0

    # check if the number of terms is valid
    if num <= 0:
        print("Please enter a positive integer")
    # if there is only one term, return n1
    elif num == 1:
        print("Fibonacci sequence upto", num, ":")
        print(n1)
    # generate fibonacci sequence
    else:
        print("Fibonacci sequence:",end=" ")
        while count < num:
            print(n1 ,end=" ")
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1
