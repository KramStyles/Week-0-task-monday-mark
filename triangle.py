def inverted_triangle(number):
    """
    This function draws a certain number of triangles in a descending order
    param : number(int) - numbers of triangles to draw
    return: triangles(str) - A string of triangles
    """

    triangles = "" # sets an empty variable to return statements

    if type(number) == int:
        # Making sure number is an integer
        for x in range(number, 0, -2):
            # 
            triangles += " * " * x + "\n"
    else:
        triangles = "Input must be a valid number"

    return triangles


print(inverted_triangle(6))
