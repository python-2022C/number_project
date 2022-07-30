class Number:
    def __init__(self,num):
        self.num = num
    def data_type(self):
        return type(self.num)
        # type -> int, str, bool, float 
    def len(self):
        return len(str(self.num)) # -> int

