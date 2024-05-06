

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

    return getCalledfunction(source_code)
    '''
    print(source_code)
    # Define the regex pattern to match function calls
    function_call_pattern = r'(\w+)\('

    # Find all matches of function calls in the source code
    matches = re.findall(function_call_pattern, source_code)

    # Filter out function names that are not defined in the global scope
    for match in matches:
        print(match)
        if match in globals() and callable(globals()[match]):
            if match != func.__name__:
                called_functions.append(match)
            
    return called_functions'''

def getCalledfunction(source_code):
    called_functions = []

    print(source_code)
    # Define the regex pattern to match function calls
    function_call_pattern = r'(\w+)\('

    # Find all matches of function calls in the source code
    matches = re.findall(function_call_pattern, source_code)

    # Filter out function names that are not defined in the global scope
    for match in matches:
        print(match)
        if match in globals() and callable(globals()[match]):
            called_functions.append(match)
            
    return called_functions
    
    
    


# Example usage
#func_a()


#print("Functions called by func_a:", get_called_functions(func_a))

#print(inspect.getmembers(myCLass, predicate=inspect.isfunction))
#print("Functions called by func_a_2:", get_called_functions2(func_a))

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

#print(find_python_functions(text))


#dd = dir(__builtins__)
#print("print" in dd)

import re

def extract_function_body(function_name, text):
    #pattern = "(def*\W(\w+)([\w\W]*?))(?=(def)|$)"
    pattern = "(def*\W("+function_name+"+)([\w\W]*?))(?=(def)|$)"
    match = re.search(pattern, text)
    
    #print(match)
    if match:
        return match.group(1)
    else:
        return None

# Example usage:
text = """
import flask
from flask import request
from zeeguu.core.user_activity_hooks.article_interaction_hooks import (
    distill_article_interactions,
)

/(def*\W(\w+)([\w\W]*?))(?=(def)|$)/g
from . import api, db_session
from zeeguu.api.utils.route_wrappers import cross_domain, with_session
from zeeguu.core.model import UserActivityData


@api.route("/upload_user_activity_data", methods=["POST"])
@cross_domain
@with_session

def upload_user_activity_data():
   
    UserActivityData.create_from_post_data(db_session, request.form, flask.g.user)

    if request.form.get("article_id", None):
        distill_article_interactions(db_session, flask.g.user, request.form)

    if request.form.get("event") == "AUDIO_EXP":
        from zeeguu.core.emailer.zeeguu_mailer import ZeeguuMailer

        ZeeguuMailer.notify_audio_experiment(request.form, flask.g.user)

    return "OK"

def hejVerden():
    print("hej verden")
"""

#function_name = "upload_user_activity_data"
#body = extract_function_body(function_name, text)
#print(body)

'''
text2 = "from zeeguu.core.model import UserActivityData"

def getImportedModules(text2):
    y = re.search("^from (\S+)", text2)
    if y: 
        basisModule = y.group(1)
        finalModuleList = []
        pattern = r"from\s+[\w.]+\s+import\s+([\w\s,]+)"
        match = re.search(pattern, text2)
        if match:
            imported_items_str = match.group(1)
            imported_items = [item.strip() for item in imported_items_str.split(",")]
            for item in imported_items: 
                finalModuleList.append(basisModule+"."+item)
            return finalModuleList
        else:
            return []
        
import re


# Example usage:
import_statement2 = "from zeeguu.core.model import UserActivityData,nogetrejde, nogetAndet"
imported_items = getImportedModules(import_statement2)
print(imported_items)

'''

'''
line = "import json, sys"
y = re.search("^import (\S+)", line)

print(y.group(1))
'''

def remove_right_until_first_slash(input_string):
    # Split the string at the last "/" and take the first part
    parts = input_string.rsplit("/", 1)
    if len(parts) > 1:
        return parts[0]
    else:
        return input_string

# Example usage:
input_string = "zeeguu-api/zeeguu/api/utils/route_wrappers.py"
result = remove_right_until_first_slash(input_string)
print(result)
