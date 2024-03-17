# Default arguments demo
def grocery(item, price=40.0):
    """To display the given arguments"""
    print("Item = %s" % item)
    print("Price = %.2f" % price)


grocery("Rice")
grocery(item="Kaju", price=677.45)