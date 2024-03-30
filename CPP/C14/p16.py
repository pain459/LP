# Duck typing example - v2.0
class Dog:
    def bark(self):
        print('Bow, wow!')


class Duck:
    def talk(self):
        print('Quack, quack!')


class Human:
    def talk(self):
        print('Hello, hi!')


def call_talk(obj):
    obj.talk()


# Call call_talk method and pass an object
x = Duck()
call_talk(x)
x = Dog()
call_talk(x)  # Error occurs in this call.