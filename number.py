import math
class Number:
    def __init__(self,num):
        self.num = num
    def data_type(self):
        return type(self.num)
        # type -> int, str, bool, float 
    def len(self):
        return len(str(self.num)) # -> int
    def is_positive(self):
        return self.num > 0 # if self.num > 0 return True ,otherwise return False
    def is_negative(self):
        return self.num < 0 # if self.num < 0 return True ,otherwise return False
    def is_zero(self):
        return self.num == 0 # if self.num = 0 return True ,otherwise return False
    def is_even(self):
        return self.num % 2 == 0 # if self.num is even return True ,otherwise return False
    def is_odd(self):
        return self.num % 2 == 1 # if self.num is odd return True ,otherwise return False
    def is_prime(self):
        for i in range(2, math.sqrt(self.num) +1):
            if self.num % i == 0:
                return False 
        return True # if self.num is prime return True ,otherwise return False
