def inverted_triangle(number):
    """
    This function draws a certain number of triangles in a descending order
    param : number(int) - numbers of triangles to draw
    return: triangles(str) - A string of triangles
    """


    if type(number) == int:
        # Making sure number is an integer
        multiplier = (number - 1) * 2
        for x in range(multiplier, 0, -2):
            print((" * " * x)[:-2] + "\n")
    else:
        print("Input must be a valid number")



inverted_triangle(6)
print("abcde"[:-1])