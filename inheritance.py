# inheritance
# users
# -Wizard
# -archers
# -ogres


class User():  # parent
    def sign_in(self):
        print('logged in')


class Wizard(User):  # child1
    def __init__(self, name, power):
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

    def run(self):
        print('Run run run fast')


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, arrows)


hb1 = HybridBorg('boggy', 50, 100)
print(hb1.attack())
print(hb1.sign_in())

# Wizard1 = Wizard('Harry', 30)
# print(isinstance(Wizard1, object))

# archer1 = Archer('Robin', 20)
# Wizard1.attack()
# archer1.attack()
