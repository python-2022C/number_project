class Number:
    def __init__(self,num):
        self.num = num

    # Create methods of Number class
    # Data type determination
    def typed(self):
        return type(self.num)
    # Finding the length of a number
    def length(self):
        return len(str(self.num))
    # determine whether it is positive
    def is_zero(self):
        return self.num == 0

        