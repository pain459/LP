# Class methods demo.
class Bird:
    # this is a class var
    x = 2

    @classmethod
    def fly(cls, name):
        print(f'{name} flies with {cls.x} wings')


# display information for 2 birds
Bird.fly(name='Sparrow')
Bird.fly(name='Bat')
Bird.x = 4
Bird.fly(name='Dragon')
Bird.fly(name='Sparrow')
Bird.fly(name='Bat')