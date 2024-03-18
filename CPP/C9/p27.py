# recursive function to solve towers of Hanoi
def towers(n, a, c, b):
    if n == 1:
        print(f'Move disk {n} from pole {a} to pole {c}')
    else:
        towers(n-1, a, b, c)
        print(f'Move disk {n} from pole {a} to pole {c}')
        towers(n-1, b, c, a)


n = int(input("Enter the number of disks: "))
towers(n, 'A', 'C', 'B')