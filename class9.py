#OOP

class PlayerCharacter:
  # Class Object Attribute
  membership = True
  # Constructer
  def __init__(self, name,age):
    if (self.membership):
      self.name = name #attributes
      self.age = age
  def run(self):
    print(f'my name is {self.name}')
    # return 'hello'

  @classmethod
  def add_num(cls, num1, num2):
    return num1 + num2



player1 = PlayerCharacter('ram',32)
print(player1.name)
print(player1.run())
print(player1.age)
print(player1.membership)


player2 = PlayerCharacter('Simanta',21)
player2.life = 50
print(player2.name)
print(player2.life)


print(PlayerCharacter.add_num(2,5))



# exercise

#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    



# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('harry',12)
cat2 = Cat('hey',21)
cat3 = Cat('ram',23)

def Oldest():
  old = cat1.age
  if (old < cat2.age and cat2.age > cat3.age):
    old = cat2.age
  elif (old < cat3.age and cat3.age > cat2.age):
    old = cat3.age

  return old


print('old cat age is '+ f'{Oldest()}')


# def get_oldest_cat(*args):
#     return max(args)
