# functions with outputs

def format_name():
    """Take a first and last name and format it to return the title case version of the name"""
    f_name = str(input('Enter the first name: '))
    l_name = str(input('Enter the last name: '))
    if f_name == "" or l_name == "":
        return "Empty firstname or lastname detected."
    full_name = f_name.title() + ' ' + l_name.title()
    return full_name


print(format_name())