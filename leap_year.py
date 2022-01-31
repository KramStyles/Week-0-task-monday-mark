def leap_year(year):
        """
        This function checks if a given year is a leap year. 
        param : year(int) - Inputted by the user
        return: result(boolean) - True or False for Leap and non leap years respectively 
        """
        if not year % 4 and str(year)[-2:] != "00":
            return True
        elif str(year)[-2:] == "00" and year% 400 == 0:
            return True
        else:
            return False

print(leap_year(1984))
print(leap_year(1985))