class College:
    def __init__(self):
        self.student_name = 'Pain'
        self.name = 'YALES'
        self.estd = 1867
        self.country = 'US'

    def student(self):
        self.student_name = 'Obu'
        self.name = 'UIUC'
        self.estd = 1900
        self.country = 'NA'
        print(self.student_name)
        print(self.name)


x = College()
x.student()
