# items = 1  # Can be accessed inside and outside the function.
# # Global scope


# def increase_items():
#     items = 2  # Only can be accesssed from inside the function.
#     # Local sope
#     print(f"Items inside the function {items}")


# increase_items()
# print(f"Items outside the function {items}")


# block scope
# game_level = 3
# enemies = ['Skeleton', 'Zombie', 'Alien']
# if game_level < 5:
#     new_enemy = enemies[0]

# print(new_enemy)

# Modifying a global variables
items = 1  # Can be accessed inside and outside the function.
# Global scope


def increase_items():
    global items  # First making this as global
    items += 2  # Then we can access this variable.
    # Local sope
    print(f"Items inside the function {items}")


increase_items()
print(f"Items outside the function {items}")
