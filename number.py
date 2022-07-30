import math

class Number:
    def __init__(self,num):
        self.number = num

    # Create methods of Number class
    def is_zero(self):
        return self.num==0


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
    def data_type(self):
        '''
        this method returns the type of the number.
        '''
        return type(self.number)

    def len(self) -> int:
        '''
        this method returns the length of the number. 

        Args:
            No
        Returns: 
            int: the length of the number.
        '''
        return len(str(self.number))

    def is_positive(self) -> bool:
        '''
        this mehtod returns true if number is positive otherwise false.

        Args:
            No
        Returns:
            bool: true if number is positive otherwise false.
        '''
        return self.number > 0

    def is_negative(self) -> bool:
        '''
        this mehtod returns true if number is negative otherwise false.

        Args:
            No
        Returns:
            bool: true if number is negative otherwise false.
        '''
        return self.number < 0

    def is_zero(self) -> bool:
        '''
        this mehtod returns true if number is zero otherwise false.

        Args:
            No
        Returns:
            bool: true if number is zero otherwise false.
        '''
        return self.number == 0

    def is_even(self) -> bool:
        '''
        this mehtod returns true if number is even number otherwise false.

        Args:
            No
        Returns:
            bool: true if number is even number otherwise false.
        '''
        return self.number % 2 == 0

    def is_odd(self) -> bool:
        '''
        this mehtod returns true if number is odd number otherwise false.

        Args:
            No
        Returns:
            bool: true if number is odd number otherwise false.
        '''
        return self.number % 2 == 1

    def is_prime(self) -> bool:
        '''
        this mehtod returns true if number is prime otherwise false.

        Args:
            No
        Returns:
            bool: true if number is prime otherwise false.
        '''

        if self.number == 2:
            return True
        for i in range(2, math.sqrt(self.num) +1):
            if self.num % i == 0:
                return False 
        return True
    
    def str_to_int(self):
        '''
        this method parse given string to integer
        Args:
            String
        Returns:
            int
        '''
        return int(str)
