import math
class Number:
    def __init__(self,num):
        self.number = num

    # Create methods of Number class
    def is_zero(self):
        return self.num==0

    # Create methods of Number class
    def length(self):
        """
        Returns length of number -> int
        """
        return len(str(self.num))

    def is_positive(self):
        return self.num > 0 # if self.num > 0 return True ,otherwise return False
    def is_negative(self):
        return self.num < 0 # if self.num < 0 return True ,otherwise return False
    def is_even(self):
        return self.num % 2 == 0 # if self.num is even return True ,otherwise return False
    def is_odd(self):
        return self.num % 2 == 1 # if self.num is odd return True ,otherwise return False
    def is_prime(self):
        for i in range(2, int(math.sqrt(self.num))+1):
            if self.num % i == 0:
                return False 
        return True # if self.num is prime return True ,otherwise return False
