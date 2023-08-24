class Array():
    def __init__ (self, lst=[]):
        self.data = list(lst)
    
    def append(self, new_element):
        self.data.append(new_element)

    def save(self, filepath):
        lst = [str(i) for i in self.data]
        with open(filepath, 'w') as f:
            f.write('\n'.join(lst))

    def load(self, filepath):
        with open(filepath, 'r') as f:
            data = f.read()
        self.data = data.split('\n')

    def __str__(self):
        return "{" + str(self.data)[1:-1] + "}"



