# Key word arguments demo
def grocery(item, price):
    """To display given numbers"""
    print("Item = %s" % item)
    print("Cost = %.2f" % price)


# Calling grocery and passing 2 arguments
grocery(item='Sugar', price=23.5)
grocery(price=44.6, item='Rice')