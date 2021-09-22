# Employee file structure
class Employee:
    DOJ = 20210101

    def __init__(self, name, age, team):
        self.name = name
        self.age = age
        self.team = team
    def __str__(self):
        return f"{self.name} has joined in {self.DOJ} and currently working in {self.team}"


employee1 = Employee("A", 33, "GTO")
employee2 = Employee("B", 31, "REC")

print(employee1.DOJ)
employee1.DOJ = 20160501

print(employee1.DOJ)
print(employee1)
