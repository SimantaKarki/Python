#methods VS function

# method s are used using ."something"
print('hello'.capitalize())

#Doc string

def test(a):
  '''
  hello i am a Doc string
  '''
  print(a)

test('!!!')

def my_function(): 
    """Demonstrate docstrings and does nothing really."""
   
    return None
  
print ("Using __doc__:")
print (my_function.__doc__) 
  
print ("Using help:")
help(my_function)

#clean code

def is_even(num):
  return num % 2 == 0
  

print(is_even(51))





