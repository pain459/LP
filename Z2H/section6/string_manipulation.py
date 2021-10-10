# if user enters "asdfg" function returns "aSdFg"

def camel_creator(a):
    x = 0
    a_camel = ''
    while x < len(a):
        for i in a:
            if x % 2 == 0:
                i = i.lower()
                a_camel = a_camel + i
                x += 1
            elif x % 2 != 0:
                i = i.upper()
                a_camel = a_camel + i
                x += 1
            else:
                pass
    print(a)
    return a_camel

a = 'asdfasfgasdfgasdfasdfgasdgd'

print(camel_creator(a))