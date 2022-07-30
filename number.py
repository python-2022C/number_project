class Number:
    def __init__(self,num):
        self.num = num
    def length(self):
        """
        Returns length of number -> int
        """
        return len(str(self.num))
    def data_type(self):
        """
        Returns data type of number -> int, float
        """
        return type(self.num)
    def is_zero(self):
        """
        Returns given number is zero or non -> bool
        """
        return self.num == 0
    def is_prime(self):
        """
        Returns given number is prime or non -> bool
        """
        nums = []
        for i in range(1, self.num+1):
            if self.num%i==0: nums.append(i)
        return len(nums) == 2
