class Programmmer():
    company = "Microsoft"

    def __init__(self, name, salary, wh):
        self.name = name
        self.salary = salary
        self.wh = wh

    def info(self):
        print(f'''Name :- {self.name}\nSalary :- {self.salary}\nWorking hours :- {self.wh}\n''')


p1 = Programmmer("Joe", "150 k", 8)
p2= Programmmer("Pradeep", "200 k", 10)

p1.info()
p2.info()
