# Key variable argument demo
def display(farg, **kwargs):
    """to display given values"""
    print("Formal argument=", farg)

    for x, y in kwargs.items():
        print(f'Key = {x}, Value={y}')


display(5, rno=12)
display(34, Name='Pain', Team='Akatsuki')