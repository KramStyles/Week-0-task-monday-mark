def factorial(number):
    """
    A function that returns the factorial of any number given to it
    param: number(int) - Number inputted by the user
    return: (str) - A string suggesting the factorial of the given number
    """

    # Ans variable to hold our answers during calculation
    ans = 1
    for x in range(1, number+1):
        # Multiplies the current index with the existing value of ans
        ans *= x
    return(f"The factorial of {number} is {ans}.")


print(factorial(4))