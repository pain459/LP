# Display start in right angled triangular form.

# Jugaad way
for i in range(10):
    print(i * "*")

# somewhat complicated way.

for i in range(1, 11):
    for j in range(1, i+1):
        print("* ", end=" ")
    print()