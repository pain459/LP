# A function to display a group of strings.
def display(lst):
    """Function to display the strings."""
    for i in lst:
        print(i)


print("Enter string separated by comma: ")
x = [i for i in input().split(',')]
display(lst=x)
