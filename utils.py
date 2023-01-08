class Utils:
    def __init__(self,numbers):
        self.numbers = numbers
    def find_max(self):
        max = 0
        for number in self.numbers:
            if(number>max):
                max = number
        return max