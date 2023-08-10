
#                                                              Directions:
# You are not allowd to use any libraries to implement this function other than the two already provided.
# Note: you may need to run "pip3 install pygrab" or  "pip3 install pandas" to install the libraries

"""
Your objective in this assignment is to complete the scrape() function. This function should make an http request 
to "https://www.worldometers.info/geography/alphabetical-list-of-countries/" and return the data for all the 
countries as a pandas data frame. 

Hint: visit the website to get a general idea of the layout before you begin. 
Hint: Read the documentation about both libraries before using them.
"""

# Once you're done, you can run this file and you will see a few tests of your code. If the output for your functions and the 
# actual output are the same, then your code is correct.

# If you need a reference, a correct implemntation of the function(s) can be found here: https://raw.githubusercontent.com/thecodingplace/assignments/main/Python/WebScrapeCountries_complete.py
# Please note that there can be several correct implementations to a function

import pygrab
import pandas as pd

def scrape(url):
    pass







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


code = pygrab.get('https://raw.githubusercontent.com/thecodingplace/assignments/main/Python/WebScrapeCountries_complete.py').text
tracker = UnitTestTracker()
for i in range (2):
    if i == 1:
        exec(code)
        tracker.add_type = 'key'
    
    tracker.add(scrape, args=["https://www.worldometers.info/geography/alphabetical-list-of-countries/"])

tracker.display()