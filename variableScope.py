# This is an example of variable scope in Python.
# A variable defined inside a function is local to that function and cannot be accessed outside of it.
# A variable defined outside of any function is global and can be accessed from anywhere in the code.

example = "Sample text" # This is a global variable

def sampleFunction():
    example = "This is called from inside the function having the same variable name" # This is a local variable
    print(example) # This will print the local variable
    return


print(example) # This will print the global variable
sampleFunction() # This will call the function and print the local variable
print(example) # This will print the global variable again, showing that it has not changed

# 1. local variables are only accessible within the function they are defined in, and cannot be accessed outside of it.

def loc_ex():
    name = "Shivam"
    return name

loc_ex()
#print(name) # This will raise an error because 'name' is a local variable and cannot be accessed outside of the function.

# 2. global variables are accessible from anywhere in the code, including inside functions.
global_var = "I am a global variable"
def global_ex():
    print(global_var) # This will print the global variable
    return
global_ex() # This will call the function and print the global variable
print(global_var) # This will print the global variable again, showing that it can be accessed from anywhere in the code.

# 3. If a local variable has the same name as a global variable, the local variable will take precedence within the function, and the global variable will be shadowed.
name = "Global Name" # This is a global variable
def shadow_ex():
    name = "Local Name" # This is a local variable that shadows the global variable
    print(name) # This will print the local variable, not the global variable
    return
shadow_ex() # This will call the function and print the local variable
print(name) # This will print the global variable, showing that it is not affected by the local variable in the function.

# 4. To modify a global variable inside a function, you can use the 'global' keyword to indicate that you want to use the global variable instead of creating a new local variable.
counter = 0 # This is a global variable     
def increment_counter():
    global counter # This tells Python that we want to use the global variable 'counter'
    counter += 1 # This modifies the global variable
    return
increment_counter() # This will call the function and increment the global variable
print(counter) # This will print the modified global variable, which should now be 1

# 5. The local variable from one function cannot be accessed in another function, even if they have the same name.
def func1():
    var = "I am a local variable in func1"
    return var
def func2():
    var = "I am a local variable in func2"
    return var

print(func1()) # This will print the local variable from func1
print(func2()) # This will print the local variable from func2
