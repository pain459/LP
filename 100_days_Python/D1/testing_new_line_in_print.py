print('This is line1\nThis is line2')
print("Trying again in line 1\nThis should be line2")
print("This time we will escape the new line.\\n This should be the same line.")  # escaping the line.
print("""This obviously don't work! \n Expecting the same line.""")  # Even this works
print('''How about now? \n yes, new line it is!''')