def inverted_triangle(number):
    """
    This function draws a certain number of triangles in a descending order
    param : number(int) - numbers of triangles to draw
    return: triangles(str) - A string of triangles
    """


    if type(number) == int:
        # Making sure number is an integer
        multiplier = (number - 1) * 2
        # Multiplier stores the double of the inputted number (less of one before multipliation)
        for x in range(multiplier, 0, -2): # For loop to print the numbers in reverse

            # Prints out the asterisx character at the center of the terminal (Couldn't get the exact center of the terminal because no libraries were imported)
            print("\n", (" * " * x)[:-2].center(100))
    else:
        # Just in case the input is not a number
        print("Input must be a valid number")



inverted_triangle(6)
