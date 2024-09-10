class calculator():
    def __init__(self, num):
        self.num = num

    def square(self):
        print("Square = ",self.num**2)

    def squareroot(self):
        print("Square Root = ",self.num**0.5)
 
    def cube(self):
        print("Cube = ", self.num**3)

    @staticmethod
    def greet():
        print("Hello welcome to Class our calculator\n")

n = int(input("Enter any Number :- "))
num = calculator(n)

num.greet()
num.square()
num.cube()
num.squareroot()




        




