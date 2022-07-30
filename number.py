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