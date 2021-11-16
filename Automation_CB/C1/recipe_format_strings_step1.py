# input data
data = [(1000, 10), (2000, 17), (2500, 170), (2500, -170)]
# printing header data for reference
print('REVENUE | PROFIT | PERCENT')
# This template aligns and display the data in the proper format
TEMPLATE = '{revenue:>7,} | {profit:>+6} | {percent:>7.2%}'

# print data rows
for revenue, profit in data:
    row = TEMPLATE.format(revenue=revenue, profit=profit, percent=profit / revenue)
    print(row)
