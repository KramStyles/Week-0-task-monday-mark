def factorial(number):
    ans = 1
    for x in range(1, number+1):
        ans *= x
    return(f"The factorial of {number} is {ans}.")


print(factorial(4))