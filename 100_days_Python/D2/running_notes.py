len('string1')
len(123456)  # doesn't work due to TypeError
len(str(123456))
"Hello"[0:3]  # subscripting.
print("Hello"[-1])

type("Hello"[-1])
type(print("Hello"[-1]))

print(type("123" + "456"))

x = "12345" + "23"
print(x)
int(x) * 2  # type conversion.

x = 123_456_789_012_3456
print(x)
type(x)


# small code with len counter.
operatorName = input('Enter your name: ')
print(f'Your name name is {len(operatorName)} characters long.')

3 * 3 + 3 / 3 - 3
