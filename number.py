
import math

class Number:
    def __init__(self,num):
        self.number = num

    def data_type(self):
        return type(self.number)

    def len(self):
        return len(str(self.number))

    def is_positive(self):
        return self.number > 0

    def is_negative(self):
        return self.number < 0

    def iszero(self):
        return self.number == 0

    def is_even(self):
        return self.number % 2 == 0
    
    def is_odd(self):
        return self.number % 2 == 1
    
    def is_prime(self):
        for i in range(2, math.sqrt(self.num) +1):
            if self.num % i == 0:
                return False 
        return True

