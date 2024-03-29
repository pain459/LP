# duck typing example
# Duck class contains talk() method
class Duck:
    def talk(self):
        print('Quack, quack!')


# Human class contains talk() method
class Human:
    def talk(self):
        print('Hello, hi!')


# This method accepts an object and calls talk() method
def call_talk(obj):
    obj.talk()


# call call_talk() method and pass an object
# depending on type of object, talk() method is executed.
x = Duck()
call_talk(x)
x = Human()
call_talk(x)