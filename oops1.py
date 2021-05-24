class Programmmer():
    company = "Microsoft"

    def __init__(self, name, salary, wh):
        self.name = name
        self.salary = salary
        self.wh = wh

    def info(self):
        print(f'''Name :- {self.name}\nSalary :- {self.salary}\nWorking hours :- {self.wh}\n''')


hero = Programmmer("Hero", "50 k", 8)
superhero = Programmmer("Superhero", "100 k", 10)

hero.info()
superhero.info()
