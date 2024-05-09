# Lets create a cookie class.

class Cookie:
    def __init__(self, color):   # Constructor
        self.color = color

    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color


cookie1 = Cookie('green')
print(cookie1.color)
print(cookie1.get_color())
cookie1.set_color('red')
print(cookie1.color)
print(cookie1.get_color())