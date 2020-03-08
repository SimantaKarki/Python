 # Functions exercise
 
def myFun(arg1, **kwargs):
  print("not of **kwarg " + arg1 )
  for key, value in kwargs.items(): 
      print ("%s == %s" %(key, value)) 
  

myFun("Hi", first ='Geeks', mid ='for', last='Geeks')


def highest_even(li):
  evens = []
  for value in li:
    if(value % 2 == 0):
      evens.append(value)
  return max(evens)



print(highest_even([10,2,3,4,8,11]))

# scope - what variable do i have acess to

#global keywords

total  = 0

def count(total):
  total = total + 1
  return total


print(count(count(count(total))))




# args and kwargs

def super_func(*args,**kwargs):
  print(kwargs)
  total = 0
  for items in kwargs.values():
    total += items
  return sum(args) + total

print(super_func(1,2,3,4,5, num1 = 5,num2 = 10))

# rule: params,*args,default parameters, **kwargs