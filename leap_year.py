def leap_year(year):
        """
        This function checks if a given year is a leap year. 
        param : year(int) - Inputted by the user
        return: result(boolean) - True or False for Leap and non leap years respectively 
        """
        if not year % 4 and str(year)[-2:] != "00":
            # Checks if the year is divisible by 4 and not a century year
            return True
        elif str(year)[-2:] == "00" and year% 400 == 0:
            # Returns true if it's a century year divisible by 400
            return True
        else:
            # Returns false if it's not a leap year
            return False

print(leap_year(1984))
print(leap_year(1985))