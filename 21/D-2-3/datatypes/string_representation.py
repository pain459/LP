# Formatting of Integers
string1 = "{0:b}".format(17)
print("Binary representation of 17 is {}".format(string1))

# Formatting of Floats
exp_r = "{0:e}".format(165.6458)
print("Exponential representation of 165.6458 is {}".format(exp_r))

# Rounding off integers
int_r = "{0:.2f}".format(1/6)
print("Rounding off the result to 2 decimal places {}".format(int_r))