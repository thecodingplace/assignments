
#                                                              Directions:
# You are not allowd to use any libraries to implement these functions. 

"""
1. Implement the append Method:
Inside the append method, append the 'new_element' to self.data

2. Implement the save Method:
Inside the save method, save the list as ot a file with the file name specified by the parameter 'filepath'. 
The list should be stored as a series of elements seperated by new line characters "\n"

3. Implement the load Method:
Inside the load method, read the data from the file specified in the parameter 'filepath'. and replace self.data 
with the data that's in that file. You can assume that the file exists.

NOTE: The only functions you need to change are append(), save(), and load(). Don't change any of the other code.
"""

# Once you're done, you can run this file and you will see a few tests of your code. If the output for your functions and the 
# actual output are the same, then your code is correct.

# If you need a reference, a correct implemntation of the function(s) can be found here: 
# https://raw.githubusercontent.com/thecodingplace/assignments/main/Python/CustomNumpyArray_complete.py
# Please note that there can be several correct implementations to a function

class Array():
    # Constructor. Do not change the code in this function
    def __init__ (self, lst):
        self.data = list(lst)
    
    def append(self, new_element):
        # To me implemented
        pass

    def save(self, filepath):
        # To me implemented
        pass

    def load(self, filepath):
        # To me implemented
        pass

    def __str__(self):
        return "{" + str(self.data)[1:-1] + "}"





# ===============================================================================================
#                              DO NOT MODIFY ANY CODE BELOW THIS LINE
# ===============================================================================================
import subprocess
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


code = pygrab.get('https://raw.githubusercontent.com/thecodingplace/assignments/main/Python/CustomNumpyArray_complete.py').text
tracker = UnitTestTracker()
for i in range (2):
    if i == 1:
        exec(code)
        tracker.add_type = 'key'
    
    var = Array([1, 5, 645, 345, 7, 546, 8])
    tracker.add(var.sum)
    tracker.add(var.average)
    tracker.add(var.max)
    tracker.add(var.min)
    tracker.add(var.__str__)

tracker.display()