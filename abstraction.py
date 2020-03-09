# Public and private


class PlayerCharacter:
    def __init__(self, name, age):
        self._name = name  # private attributes
        self._age = age

    def Speak(self):
        print(f'hi, i am {self._name} and i am {self._age} yers old.')


player1 = PlayerCharacter('Simanta', 21)
player1.Speak()
