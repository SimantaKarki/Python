#loops
for item in [1,2]:
  for x in['a','b','c','d']:
    print(item,x)

#iterable
#objects that can be iterable over
#iterable can be list tuple set string

#dictionary as iterable
user = {
  'name': 'simanta',
  'age': 21,
  'can_swim' : True
}

for key,value in user.items():
  print(key,value)

for i in user.items():
  print(i)


for i in user.values():
  print(i)

for i in user.keys():
  print(i)

counter

my_list = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for i in my_list:
  sum += i
print(sum)

for i in range(10,0,-1):
  print(i)

for j in range(2):
  print(list(range(2)))

for i,char in enumerate("Hello"):
  print(i,char)

while loop

while condition:
  do something

i = 0
while i < 10:
  print(i)
  i=i+1
print(i)

break continue pass
my_list = [1,2,3,4,5]
for item in my_list:
  continue
  print(item)

i = 0
while i < len(my_list):
  print(my_list[i])
  i+=1
  pass

# GUI python







