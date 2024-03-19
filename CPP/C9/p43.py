# calculate gross and net salary with basic salary input
# dearness_allowance = 80% of basic
def da(b_salary):
    return b_salary * 0.8


# hra is 15% of basic
def hra(b_salary):
    return b_salary * 0.15


# pf is 12% of basic
def pf(b_salary):
    return b_salary * 0.12


# tax is 10 % on gross
def tax(g_salary):
    return g_salary * 0.1


basic_salary = float(input("Enter your basic salary: "))
print(f'Your basic salary is {basic_salary}')
# gross = basic + da + hra
gross_salary = basic_salary + da(basic_salary) + hra(basic_salary)
print(f'Your gross salary is {gross_salary}')
# net = gross - pf - tax
net_salary = gross_salary - pf(basic_salary) - tax(gross_salary)
print(f'Your net salary is {net_salary}')