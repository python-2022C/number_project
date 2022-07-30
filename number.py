import math
class Number:
    def __init__(self,num):

        self.number = num

    # Create methods of Number class
    def iszero(self):
        if self.number == 0:
            return True
        return False 



    # Create methods of Number class
    def length(self):
        """
        Returns length of number -> int
        """
        return len(str(self.num))
    def len(self):
        return len(str(self.num)) # -> int
    def is_positive(self):
        """
        if self.num > 0 return True ,otherwise return False
        """
        return self.num > 0 
    def is_negative(self):
        return self.num < 0 
        """
        if self.num < 0 return True ,otherwise return False
        """
    def is_even(self):
        return self.num % 2 == 0 
        """
        if self.num is even return True ,otherwise return False
        """
    def is_odd(self):
        return self.num % 2 == 1 
        """
        if self.num is odd return True ,otherwise return False
        """
    def is_prime(self):
        if self.num == 2:
            return True
        # this code returns 2 as false because 2%2==0 True
        for i in range(2, math.sqrt(self.num) +1):
            if self.num % i == 0:
                return False 
        return True 
        """
        if self.num is prime return True ,otherwise return False
        """