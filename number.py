class Number:
    def __init__(self,num):
        self.number = num

    # Create methods of Number class
    def iszero(self):
        if self.number == 0:
            return True
        return False