class Library:
    def __init__(self, booklist):
        self.books = booklist

    def display_availiable_books(self):
        print("Availiable Books are:- ")
        for book in self.books:
            print("\t* " + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}'s Book \nPlease Return it timely")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry! the book is not availible right now")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning th book. Hope you enjoyed !")


class Student:
    def requestBook(self):
        self.book = input("Enter the name of the Book you want to borrow: ")
        return self.book
    
    def returnBook(self):
        self.book = input("Enter the name of the Book you want to return: ")
        return self.book

if __name__ == "__main__":
    centralLibrary = Library(["Math", "Science", "Opt Math", "Python"])
    student = Student()
    while True:
        welcomeMsg = '''\n====== WELCOME TO CENTRAL LIBRARY =====
        Please choose an option :
        1. Listing all the books
        2. Requst a book
        3. Donate\Return a book
        4. Exit the Library
        '''
        print(welcomeMsg)
        a = int(input("Enter your choice:- "))

        if a == 1:
            centralLibrary.display_availiable_books()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing Central Library")
            exit()
        else:
            print("Invalid !!! Choice")
