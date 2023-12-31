
#                                                              Directions:
# You are not allowd to use any libraries to implement these functions. 

"""
1. Implement the sum Method:
Inside the sum method, calculate the sum of all the elements in the self.data list.
You can use the built-in sum function or a loop to achieve this.
Return the calculated sum.

2. Implement the average Method:
Inside the average method, calculate the average of the elements in the self.data list.
You can use the sum method you implemented earlier and divide it by the length of the list.
Return the calculated average.

3. Implement the min Method:
Inside the min method, find the minimum value in the self.data list.
You can use the built-in min function or a loop to achieve this.
Return the minimum value.

4. Implement the max Method:
Inside the max method, find the maximum value in the self.data list.
You can use the built-in max function or a loop to achieve this.
Return the maximum value.

5. Implement the __str__ Method:
Inside the __str__ method, you need to create a string representation of the self.data list but with curly braces instead of square brackets.
You can use string concatenation or a loop to build the string.
Start with a left curly brace "{, then add the elements of the list separated by commas and spaces, and finally add a right curly brace }".
Return the resulting string.


NOTE: The only functions you need to change are sum(), average(), min(), max(), and __str__(). Don't change any of the other code.
"""

# Once you're done, you can run this file and you will see a few tests of your code. If the output for your functions and the 
# actual output are the same, then your code is correct.

# If you need a reference, a correct implemntation of the function(s) can be found here: https://raw.githubusercontent.com/thecodingplace/assignments/main/Python/CustomNumpyArray_complete.py
# Please note that there can be several correct implementations to a function

class Array():
    # Constructor. Do not change the code in this function
    def __init__ (self, lst):
        self.data = lst
    
    def sum(self):
        # To me implemented
        pass

    def average(self):
        # To me implemented
        pass

    def min(self):
        # To me implemented
        pass

    def max(self):
        # To me implemented
        pass

    # This __str__ method should return a string version of the list with curly braces instead of squre brackets
    # Example: if self.data = [1, 2, 3], the __str__ method should return "{1, 2, 3}"
    def __str__(self):
        result_string = ""
        # To be implemented
        return result_string









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