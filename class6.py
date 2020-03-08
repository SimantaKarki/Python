picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

for row in picture:
  for j in row:
    if (j == 1):
      print('*',end='')
    else:
      print(' ' ,end='')
  print('')



some_list = ['a','b','c','b','d','m','n','n']

duplicates = []
for value in some_list:
  if some_list.count(value) > 1:
    if value not in duplicates:
      duplicates.append(value)

print(duplicates)

functions

def say_hello():
  print('Hello i am a function')

for i in range(2):
  say_hello()

#parameters vs arguments

#parameters
def say_hello(name,emoji):
  print(f'Hey {name} {emoji}')

#arguments
say_hello('Simanta',':)')

# keywords arguments
say_hello(emoji = ':)',name = "Karki")

#default parameter
def call_hello(name = 'Shreya',emoji = '(:'):
  print(f'hello {name} {emoji}')
call_hello()

# #return
def sum(num1,num2):
  def another_func(n1,n2):
    return n1+n2
  return another_func(num1,num2)

print(sum(2,5))






