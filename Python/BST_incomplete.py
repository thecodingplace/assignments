
#                                                              Directions:
# You are not allowd to use any libraries to implement this class.

"""
Your objective in this assignment is to complete the BST() class below. The BST (Binary Search Tree) class should be able to perform the following operations:

Initialization (__init__): You should be able to initialize the BST with an optional list of data. If provided, the data should be inserted into the BST in the order given.

Add (add): This method should take a data value and insert it into the BST according to the binary search tree property.

Contains (contains): This method should take a target value and return True if the target is in the BST, and False otherwise.

To List (to_list): This method should return a list of all the data in the BST, in ascending order.

To List Helper (__to_list_helper): This private method is a helper function for the to_list method. You may use it to implement the functionality of to_list, or you may choose to implement to_list in a different way.

Please make sure to adhere to the principles of object-oriented programming and encapsulate the Node class within the BST class.

Remember, you are not allowed to use any external libraries, and your implementation should be done using only basic Python constructs.

Good luck!
"""

# Once you're done, you can run this file and you will see a few tests of your code. If the output for your functions and the 
# actual output are the same, then your code is correct.

# If you need a reference, a correct implemntation of the function(s) can be found here: https://raw.githubusercontent.com/thecodingplace/assignments/main/Python/BST_complete.py
# Please note that there can be several correct implementations to a function

class BST():
    class Node():
        def __init__ (self, data):
            pass
    
    def __init__ (self, data=[]):
        pass
    
    def add(self, data):
        pass

    def contains(self, target):
        pass

    def to_list(self):
        pass

    def __to_list_helper(self, curr, target):
        pass





# ===============================================================================================
#                              DO NOT MODIFY ANY CODE BELOW THIS LINE
# ===============================================================================================
import subprocess
import numpy as np
try: 
    import pygrab
except:
    subprocess.run("pip3 install pygrab", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    import pygrab

class UnitTestTracker():
    def __init__(self):
        self.functions = []
        self.student_ans = []
        self.ans_key = []
        self.add_type = 'attempt'
    
    def add(self, func, args=[]):
        try:
            res = func(*args)
        except Exception as err:
            res = f'Error in function {func.__name__}() : {err}'
        
        if self.add_type.lower() == 'key':
            self.ans_key.append(res)
            self.functions.append(func)
        elif self.add_type.lower() == 'attempt':
            self.student_ans.append(res)

    def display(self):
        template = "====================  Function Name  ======================\n\nNAME()\n\n======================  Your Answer  ======================\nATTEMPT\n\n====================  Correct Result  =====================\nANSWER\n\n===========================================================\n\n\n\n\n\n\n\n\n\n\n\n\n"
        result = ""
        for attempt, ans, func in zip(self.student_ans, self.ans_key, self.functions):
            result += template.replace("NAME", str(func.__name__).strip()).replace("ATTEMPT", str(attempt).strip()).replace("ANSWER", str(ans).strip())
        print(result)


code = pygrab.get('https://raw.githubusercontent.com/thecodingplace/assignments/main/Python/BST_complete.py').text
tracker = UnitTestTracker()
for i in range (2):
    if i == 1:
        exec(code)
        tracker.add_type = 'key'
    
    for i in range (3):
        lst = list((np.random.rand(40) * 100 - 50).astype(int))
        bst = BST(lst)

        tracker.add(bst.to_list, args=[])

tracker.display()