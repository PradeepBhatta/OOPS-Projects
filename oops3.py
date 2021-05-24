class Buss:
    
    def __init__(self, name, seats, fare):
        self.name = name 
        self.seats = seats
        self.fare = fare
        print(f"   {self.name} Sewa")
        print("*********************")

    @staticmethod
    def loopp(bus_name):
        while input("Do u want to book a ticket ?\n(Y for Yes and N for No) == ").lower() == "y":
            bus_name.bookTicket()
            bus_name.getSeats()
            bus_name.fares()
            global lst
            lst = []
            for i in range(st_no):
                lst.append(i)

            dc = input("Do u want to cancel a ticket ?\n(Y for Yes and N for No) == ")
            if dc.lower() == "y":
                print()
                bus_name.cancelTicket()
            else:
                print()
                continue


    def bookTicket(self):
        if self.seats > 0 :
            print("\nYour seat has been sucessffully booked")
        else:
            print("Sorry Seats are full")


    def cancelTicket(self):
        cancel = int(input("Which Ticket no. do u want to cancel :- "))
        lst.remove(cancel)
        print("Succesfully Cancelled!!! \nYour money will be deposited back to your account.\n")


    def getSeats(self):
        global st_no
        st_no = 16 - self.seats
        print(f"Your seat no.  = {st_no}")


    def fares(self):
        print(f"Rs. {self.fare} has been deducted from your account as Bus fare")
        self.seats = self.seats - 1
        print(f"No of remaining seats :- {self.seats}\n")


KailaliBus = Buss("Kailai Bus", 15, 500)
Buss.loopp(KailaliBus)
