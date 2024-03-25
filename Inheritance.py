

class Dog: #original class is the parent class
    legs = 4
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(self.name + 'says: Bark!')


    def getLegs(self):
        return self._legs

class Chihuahua(Dog): #extends the parent thus being the child class
    def speak(self):
        print(f'{self.name} says: Yap yap yap!')

    def wagTail(self):
        print('Vigorous wagging')


dog = Chihuahua('Roxy')
dog.speak()
dog.wagTail()


