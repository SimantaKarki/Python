# #password checker

print('*' * 10)
username = input('enter your username')
password = input('enter the password')
password_length = len(password)
hidden_password = '*' * password_length

# # print(f'{username}, your password {hidden_password} is {len(password)} letter long')

# #list
li = [1,2,3,4,5]
li2 = ['Simanta' 'Kushal' 'Sirish' 'Krishna']
li3 = [1,2,'simanta']
print(li3[2])

print(len(li))

# # list slicing
item = ['laptops','mobiles','gears','cosmetic','random']
item[0] = 'gum'
new_item = item
new_item[0] = 'bat' 
print(new_item)
print(item) 

#matrix multideimensional list
matrix = [
  [1,2,3,],
  [4,5,6],
  [7,8,9]
]
print(matrix[2][0])


basket = [1,3,2,4,5,6,7,8]
basket.append(100)
basket.insert(2,0)
print(basket)
basket.sort()
print(basket)

basket.remove(100)
print(basket)
print(basket.pop())

basket = ['a','b','c','d','e','f','d']
print(basket.index('b',0,5))
print('a' in basket)
print('simanta' in "karki simatna")

print(basket.count('d'))
new_basket = sorted(basket)
print(sorted(basket))
print(new_basket)

print(basket[::-1])

print(list(range(0,100)))

sentence = ' '
new_sentence = sentence.join(['hi', 'my', 'name', 'is','karki'])
print(new_sentence)

#list unpacking
a,b,c, *other,d = [1,2,3,4,5,6,7,8,9]
print(a)
print(other)
print(b)
print(c)
print(d)


#Dictionary
user = {
  'basket' : [1,2,3,],
  'greet' : 'hello',
  'age' : 20
}
print(user.get('age',20))

print('basket' in user)
print(20 in user.values())
print(user.items())
user2 = user.copy()
print(user.clear())
user2.popitem()
print(user2)

#tuples
my_tuple = (1,2,3,4,5,6)
print(my_tuple[0])
print(7 in my_tuple)

my_tuple2 = ((1,2,3),(3,2,1))
print(my_tuple2[0][1])

new_tuple = my_tuple[1:2]
print(new_tuple)

x,y,z, *other = (1,2,3,4,5,6,7,8)
print(other)
print(other.index(7))

#set data type
my_list = [1,2,3,4,5,5]
print(my_list)
print(set(my_list))
my_set = {1,2,3,4,5,6}
print(my_set)
my_set.add(100)
my_set.add(78)
print(my_set)
print(1 in my_set)
print(list(my_set))
my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

print(my_set.discard(3))
print(my_set)

print(my_set.intersection(your_set))
print(my_set & your_set)

print(your_set.union(my_set))


print(my_set.difference(your_set))
print(your_set.difference(my_set))
print(my_set.difference(my_set))


 



