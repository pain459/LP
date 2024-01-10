# Find LCM of two given numbers

def find_lcm(a, b):
    global greater
    if a > b:
        greater = a
    elif b > a:
        greater = b
    while True:
        if (greater % a == 0) and (greater % b == 0):
            lcm = greater
            break
        greater += 1

    return lcm


print(find_lcm(10, 12))
