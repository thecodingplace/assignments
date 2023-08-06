class Array():
    def __init__ (self, lst):
        self.data = lst
    
    def sum(self):
        return sum(self.data)

    def average(self):
        return sum(self.data) / len(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)
    
    def __str__(self):
        return '{' + str(self.data)[1:-1] + '}'
