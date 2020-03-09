# Encapsulation
class PlayerCharacter:
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def Speak(self):
		print(f'hi, i am {self.name} and i am {self.age} yers old.')

player1 = PlayerCharacter('Simanta',21)
player1.Speak()

player2 = {'name': 'Simanta', 'age': 200}
print(player2['name'])

