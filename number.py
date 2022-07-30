import re


class Number:
    def __init__(self,num):
        self.num = num

    # Create methods of Number class

    def data_taype(self) ->type:
        """
        function that returns the type of the number
        """
        return type(self.num)

    def number_len(self) ->len:
        """
        a function that returns the length of a number
        """
        return len(str(self.num))

    def is_positive(self) ->bool:
        """
        function that checks the positivity of a number
        """
        if self.num > 0:
            return True

    def is_negative(self) ->bool:
        """
        function that checks the negativity of a number
        """
        if self.num < 0:
            return True
    
    def is_zero(self) -> bool:
        """checking that the number is zero
        """
        if self.num == 0:
            return True
    
    def is_even(self) ->bool:
        """
        a function that determines the evenness of a number
        """
        if self.num % 2 == 0:
            return True
        else:
            return False

    def is_odd(self) ->bool:
        """
        a function that determines the oddness of a number
        """
        if self.num % 2 == 1:
            return True
        else:
            return False
    def is_prime(self):
      """a function that checks the integrity of a number"""
        for i in range(2, math.sqrt(self.num) +1):
            if self.num % i == 0:
                return False 
        return True # if self.num is prime return True ,otherwise return False

