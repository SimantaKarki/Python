

class User(object):  # parent
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')

    # def attack(self):
    #     print('Do nothing i am default')


class Wizard(User):  # child1
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking power of {self.name} is {self.power}')


class Archer(User):  # child2
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'no of arrows of {self.name} is {self.num_arrows}')


Wizard1 = Wizard('Harry', 30, 'harry@gmail.com')
# archer1 = Archer('Robin', 20)


# def player_attack(char):  # poly1
#     char.attack()


# player_attack(Wizard1)
# player_attack(archer1)

print(Wizard1.email)

# for char in [Wizard1, archer1]:  # poly2
#     char.attack()
