import math

class Number:
    def __init__(self,num):
        self.number = num

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
        for i in range(2, int(math.sqrt(self.number)) +1):
            if i % i == 0:
                return False 
        return True
    
    def int_to_str(self) -> str:
        '''
        this method converts to string.
        
        Args:
            No
        Returns:
            str: convert to string
        '''
        return str(self.number)
