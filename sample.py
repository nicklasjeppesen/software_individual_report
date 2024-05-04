

#import user
import inspect
import re

'''
def methods_in_class(cls):
	return [
		(name, object) 
		for (name, object) 
			in cls.__dict__.items() 
		if hasattr(object, '__call__')]

user = user.User()

methods_in_class(user)
'''

class myCLass: 
    def my_class_func_a():
        #print("Inside func_a")
        myclass_func_b()

    def myclass_func_b():
        print("Inside func_b")




def func_a():
    #print("Inside func_a")
    func_b()

def func_b():
    print("Inside func_b")

def get_called_functions(func):
    called_functions = []

    # Get the source code of the function
    source_lines, _ = inspect.getsourcelines(func)
    source_code = ''.join(source_lines)

    # Find all function calls in the source code
    function_calls = inspect.getmembers(func, predicate=inspect.isfunction)
    for name, _ in function_calls:
        if name != func.__name__:
            if name in source_code:
                called_functions.append(name)

    return called_functions

def get_called_functions2(func):
    called_functions = []

    # Get the source code of the function
    source_lines, _ = inspect.getsourcelines(func)
    source_code = ''.join(source_lines)

    # Define the regex pattern to match function calls
    function_call_pattern = r'(\w+)\('

    # Find all matches of function calls in the source code
    matches = re.findall(function_call_pattern, source_code)

    # Filter out function names that are not defined in the global scope
    for match in matches:
        if match in globals() and callable(globals()[match]):
            if match != func.__name__:
                called_functions.append(match)
            
    return called_functions




# Example usage
func_a()


#print("Functions called by func_a:", get_called_functions(func_a))

print(inspect.getmembers(myCLass, predicate=inspect.isfunction))
#print("Functions called by func_a_2:", get_called_functions(func_a))

#func_a.__getattribute__.__name__



def find_python_functions(text):
    pattern = r"def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\([^()]*\)\s*:"
    matches = re.findall(pattern, text)
    return matches

# Example usage:
text = """
def hello_world():
    print("Hello, world!")

def add(a, b):
    return a + b
"""

print(find_python_functions(text))
