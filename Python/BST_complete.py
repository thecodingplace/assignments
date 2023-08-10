class BST():
    class Node():
        def __init__ (self, data):
            self.data = data
            self.right = None
            self.left = None
    
    def __init__ (self, data=[]):
        self.root = None
        for i in data:
            self.add(i)
    
    def add(self, data):
        if self.root is None:
            self.root = self.Node(data)
            return
        
        curr = self.root

        while True:
            if data >= curr.data:
                if curr.right is None:
                    curr.right = self.Node(data)
                    break
                else:
                    curr = curr.right
            else:
                if curr.left is None:
                    curr.left = self.Node(data)
                    break
                else:
                    curr = curr.left

    def contains(self, target):
        curr = self.root

        while True:
            if target > curr.data:
                if curr.right is None:
                    return False
                else:
                    curr = curr.right
            elif target < curr.data:
                if curr.left is None:
                    return False
                else:
                    curr = curr.left
            else:
                return True

    def to_list(self):
        res = []
        self.__to_list_helper(self.root, res)
        return res

    def __to_list_helper(self, curr, target):
        if curr is None:
            return
        
        self.__to_list_helper(curr.left, target)
        target.append(curr.data)
        self.__to_list_helper(curr.right, target)
