class Array():
    # Constructor. Do not change the code in this function
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

    # This __str__ method should return a string version of the list with curly braces instead of squre brackets
    # Example: if self.data = [1, 2, 3], the __str__ method should return "{1, 2, 3}"
    def __str__(self):
        return '{' + str(self.data)[1:-1] + '}'
