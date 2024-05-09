from datetime import datetime, timedelta
import random
import unittest

class Book:
    """
    Represents a book in a library.
    """
    def __init__(self, book_title, author, copies):
        self.book_title = book_title
        self.author = author
        self.copies = copies
        self.waitlist = []

    def add_to_waitlist(self, a_customer, library_id):
        """
        Add a customer to the waitlist for a book.

        Args:
            a_customer (Customer): The customer to be added to the waitlist.
            library_id (Library): The library containing the book.

        Returns:
            list or None: The updated waitlist if the customer is successfully added,
                otherwise None.

        Edge Case:
            Modifies the waitlist of the book and the books_on_waitlist attribute of the customer.

        """    
        # if a customer doesn't have a library card, they can't be added to thr waitlist
        if a_customer.library_card is None:
            print("Customer has no card on file")
            return None
        # if the book title the customer wants isn't in the library system, they can't check out a book
        if self.book_title is not library_id.book_title:
            print("Book not found in library records")
            return None
        # if there are availible copies, they be added to the waitlist... because duh
        if self.copies > 0:
            print(f"There are available copies of {self.book_title}, {a_customer.name} cannot be added to waitlist")
            return None
        # if the customer is already on the waitlist, they shouldn't be added again
        if a_customer in self.waitlist:
            print(f"{a_customer.name} is already on the waitlist for {self.book_title}")
            return None
        # check the len of the books on the customer's waitlist to see if they have reached their limit
        if len(a_customer.books_on_waitlist) >= 5:
            print(f"{a_customer.name} is already on waitlist waiting for 5 books")
            return None
        
        # after are the conditions are met the customer can now be added to the waitlist
        # and they will add the book to the books on their waitlist and the method
        # will return the waitlist for other methods
        self.waitlist.append(a_customer)
        a_customer.books_on_waitlist.append(self.book_title)
        print(f"{a_customer.name} added to waitlist for {self.book_title}")
        return self.waitlist


    def remove_from_waitlist(self, a_customer):
        """
        Remove a customer from the waitlist for the book.

        Args:
            a_customer (Customer): The customer to be removed from the waitlist.

        Returns:
            list or None: The updated waitlist if the customer is successfully removed,
                otherwise None.

        Edge Case:
            Modifies the waitlist of the book when the customer is revoed from the list of customers in the library.
        """
        # Check if there are customers on the waitlist
        if self.waitlist:
            print(f"{a_customer.name} has been removed from waitlist for {self.book_title}")
            print(f"Email sent to {a_customer.email} about {self.book_title}")
            # Iterate through the waitlist and print messages for customers who need to be moved up
            for index, customer in enumerate(self.waitlist, start=1):
                # Check if the current customer is not the one being removed
                if customer != a_customer:
                    print(f"Moving {customer.name} up in the waitlist")
            # Remove the customer from the waitlist
            self.waitlist.remove(a_customer)
            # Return the updated waitlist
            return self.waitlist
        else:
            # Print a message indicating that the waitlist is empty
            print("Waitlist is empty")
            # Return None since there is no waitlist to return
            return None
            
class Customer:
    """A class to represent a library customer."""

    def __init__(self, first_name, last_name, email):
        """
        Initialize a customer with their first name, last name, and email.

        Args:
            first_name (str): The first name of the customer.
            last_name (str): The last name of the customer.
            email (str): The email address of the customer.
        """
        self.name = first_name + " " + last_name
        self.email = email
        self.library_card = None
        self.books_on_waitlist = []
        self.late_fees = 0


class Library:
    """A class to represent a library."""

    def __init__(self):
        """
        Initialize a library with its attributes and load books from a file.
        """
        self.customers = []
        self.checkedout_books_on_file = {}
        self.books_on_file = []
        self.return_date = None
        self.due_date = None

        # Load books from a file
        file_name = 'library.txt'
        with open(file_name, 'r') as file:
            for line in file:
                parts = line.strip().split(', ')
                book_title = parts[1]
                author = parts[2]
                copies = int(parts[3])
                book = Book(book_title, author, copies)
                self.books_on_file.append(book)

    def add_customer(self, customer):

        """
        Add a new customer to the library.

        Args:
            customer (Customer): The customer object to be added.

        Returns:
            Customer or None: The added customer object if successfully added, None otherwise.
        """
        ascii_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        customer.name = customer.name.replace(" ", "")

        if ascii_letters.find(customer.name) == -1:
            print(ascii_letters.find(customer.name))
            return None
         # condition if the customer is not in the library system, it gives them a randomized libary card
        # Once given library card, adds them to a list of customers in the library
        if customer not in self.customers:
            new_library_card = "{:05d}".format(random.randint(10000, 99999))
            customer.library_card = new_library_card
            self.customers.append(customer)
            print(f"Customer added with library card number {customer.library_card}")
            return customer
        return None

    def remove_customer(self, book, customer):
        """
        Remove a customer from the library.

        Args:
            book (Book): The book object.
            customer (Customer): The customer object to be removed.

        Returns:
            str or None: The library card number of the removed customer if successfully removed, None otherwise.
        """      
        # base case to remove customer because they dont exist in the library system
        if customer not in self.customers:
            print("Customer not found")
            return None
        # case where if the customer has more than 10 dollars in late fees, they are removed from the library system
        # edge case where once where they are removed from the library system they are removed from the waitlist for the book
        if self.calculate_late_fees(book.book_title) > 10:
            self.customers.remove(customer)
            for c in customer.waitlist:
                if customer is c:
                    customer.waitlist.remove(customer)
                    print(f"{customer.name} removed from the waitlist for book: {book.book_title}")
            print(f"Customer with library card {customer.library_card} removed due to excessive late fees.")
            return customer.library_card

        else:
            print(f"Customer with library card {customer.library_card} has {customer.late_fees} late fees, which is within the allowed limit.")
            return None
    
    def checkout_book(self, book_title, my_customer, checkedout_book):
        """
        Checking if the book the customer wants is in the library and checking if the customer has a library card first before they are able to checkout.
        During checkout, customer will get a due date.
        If there are no more available copies in the library, the book will be added to add_to_waitlist.
        Parameters:
            book_title (str): the title of the book in library txt file
            my_customer (str): the first and last name of the customer
            checkedout_book (str): the title of the book the customer has checked out

        Return:
            checkout_date (date): the date the customer checked out the book
            self.due_date (date): the date the customer has to return the book by for no late fees 
            book_title (str): the title of the book in library txt file
        """
        in_library = False
        is_customer = False
        # Checking if the book the customer wants is on file and if the customer has a library card.
        for book in self.books_on_file :
            if book.book_title == book_title:
                in_library = True
        for person in self.customers :
            if person.name == my_customer.name:
                is_customer = True 
        # If the book is not in the library, print message and return none      
        if not in_library:
            print("The library doesn't have this book")
            return None
        # If the customer is does not have a library card, print message and return none
        if not is_customer:
            print(f"{my_customer.name} doesn't have a library card")
            return None
        global checkout_date
        global due_date
        global book_info    
        # Creating a checkout date and due date
        checkout_date = datetime.today()
        self.due_date = checkout_date + timedelta(days=15)
        book_info = {
            'name': my_customer.name,
            'book_title': book_title,
            'checkout_date': checkout_date,
            'due_date': self.due_date,
        }
        print(f"Librarian is processing book")
        # If there are no more available copies left, return none, if there are, take one copy out of the library
        if checkedout_book.copies <= 0:
            print(f"Sorry, no available copies of {book_title}")
            checkedout_book.add_to_waitlist(my_customer, checkedout_book)
            return None       
        else :
            checkedout_book.copies -= 1
        # Successfully checking out the book, printing out message, returning checkout_date, due_date, and book_title
            if book_title not in self.checkedout_books_on_file:
                self.checkedout_books_on_file[book_title] = [book_info]
            else:
                self.checkedout_books_on_file[book_title].append(book_info)            
        print(f"{my_customer.name} has checked out {book_title} on {checkout_date}. Book is due on {self.due_date}")
        return checkout_date, self.due_date, book_title



    def return_book(self, book_title, book, customer):
        """
        Checking if the book the customer wants to return matches in the file. 
        If the customer returns the book after the due date, late fees will occur.

        Parameters:
            book_title (str): the title of the book in the library txt file
            book (obj): the Book object itself
            customer (obj): the Customer object
        """
        # Checking if the book the customer is returning is on file, if it is, get the checkout date and creating a list of the book checked out
        if book_title in self.checkedout_books_on_file:
            get_checkout_date = ""
            checkedout_book_arr = self.checkedout_books_on_file[book_title]
            index = 0
            # removing the book the customer is returning 
            for i in range (len(checkedout_book_arr)):
                if checkedout_book_arr[i]['name'] == customer.name:
                    index = i
                    get_checkout_date = checkedout_book_arr[i]['checkout_date']

            checkedout_book_arr.pop(index)
            # If the customer returns the book after 15 days (random), late fees will occur
            self.return_date = get_checkout_date + timedelta(days= 45 * random.random())
            print(f"Return date for {book_title} is {self.return_date}")
            self.calculate_late_fees(book_title)
            book.copies += 1

            return self.return_date
        
        print("This book has not been checked out")
        return None
    
    def calculate_late_fees(self, book_title):
        """
        Checks if a customer's returned book would have late fees. If the customer's
        book was returned by the due date, customer won't have any late fees. If
        customer's book was returned late, the late fee will be calculted.

        Parameters:
            book_title (str): the title of the book that the late fee is being 
            calculated for.
            
        Return:
            float: the amount for the late fee, or 0 if there is no late fees
        """
        
        get_due_date = self.due_date
        if self.return_date is not None:
            days_late = abs((self.return_date - get_due_date).days)
            print(f"{book_title} is {days_late} days late")
            if days_late > 0:
                late = days_late * 0.50
                print(f"Customer needs pay ${late}")
                return int(late)
        else:
            late = 0
            print(f"Customer is fine")
            return int(late)
    
class UnitTests(): 
    """
    Class for all unit tests that are called after certain calls in main method 
    are made.
    """
    def test_library_books_on_file():
        assert (len(library.books_on_file) == 18)
    def test_add_first_2customers():
        assert(len(library.customers) == 2)
    def test_checkout_1Moby_Dick():
        assert(library.checkedout_books_on_file["Moby Dick"] != None)
        assert(book1.copies == 9)
    def test_checkout_book_edge_cases():
        assert(library.checkout_book("The Giver", customer2, book_not_in_lib) == None)
        assert(library.checkout_book("Peter Pan", customer3, book2) == None)
    def test_checkout_all_Moby_Dick():
        assert(book1.copies == 0)
        assert(library.checkout_book("Moby Dick", customer1, book1) == None)
        assert(len(library.checkedout_books_on_file["Moby Dick"]) == 9)
    def test_add_waitlist():
        assert(len(book1.waitlist) == 1)
    def test_return_book_edge_cases():
        assert(library.return_book("Oliver Twist", book1, customer2) == None)
        assert(library.return_book("Moby Dick", book1, customer1) != None)

if __name__ == "__main__":
    tests = UnitTests()
    # creates new Library instance that'll be used for rest of main
    library = Library()
    print("Open library system")
    tests.test_library_books_on_file()

    # creates new Customers instances and adds them to library  
    customer1 = Customer("Sam", "Puckett", "spuck@gmail.com")
    customer2 = Customer("Fred", "Benson", "fredben@gmail.com")
    customer3 = Customer("Carly", "Shay", "icarlyshay@gmail.com")

    library.add_customer(customer1)
    library.add_customer(customer2)
    tests.test_add_first_2customers()

    # check out books that exist in library.txt
    book1 = Book("Moby Dick", "Herman Melville", 10)
    book2 = Book("Peter Pan", "J.M. Barrie", 10)
    book3 = Book("Oliver Twist", "Charles Dickens", 10)
    book_not_in_lib = Book("The Giver", "Chris Evans", 10)

    library.checkout_book("Moby Dick", customer1, book1)
    tests.test_checkout_1Moby_Dick()
    tests.test_checkout_book_edge_cases()

    for i in range(9):
        library.checkout_book("Moby Dick", customer1, book1)
    tests.test_checkout_all_Moby_Dick()
    tests.test_add_waitlist()
    tests.test_return_book_edge_cases()
