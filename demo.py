import unittest
from datetime import datetime, timedelta
import random

class Book:
    def __init__(self, book_title, author, copies):
        self.book_title = book_title
        self.author = author
        self.copies = copies
        self.waitlist = []

    def add_to_waitlist(self, a_customer, library_id):
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
            self.waitlist.pop(a_customer)
            # Return the updated waitlist
            return self.waitlist
        else:
            # Print a message indicating that the waitlist is empty
            print("Waitlist is empty")
            # Return None since there is no waitlist to return
            return None
            
class Customer:
    def __init__(self, first_name, last_name, email, phone):
        self.name = first_name + " " + last_name
        self.email = email
        self.library_card = None 
        self.books_on_waitlist = []
        self.late_fees = 0
       
class Library:
    def __init__(self):
            # self.customers = {}
            # self.checked_out_books_on_file = {}
            # self.copies = {}
        self.customers = []
        self.checkedout_books_on_file = {}
        self.books_on_file = []
        self.return_date = None
        self.due_date = None

    def add_customer(self, customer):
        if customer not in self.customers:
            new_library_card = "{:05d}".format(random.randint(10000, 99999))
            customer.library_card = new_library_card
            self.customers.append(customer)
            print(f"Customer added with library card number {customer.library_card}")
            return customer
        return None

    
    def remove_customer(self, library_card, customer): 
        customer = Customer()
        customer_name = customer.name #name of customer that
        
        if self.calculate_late_fees > 10: #figure out threshhold
            self.customers.remove(customer)
            # self.customers.remove(customer)
            print(f"Customer with library card {customer.library_card} removed due to excessive late fees.")
            return None
        else:
            print(f"Customer with library card {customer.library_card} has {customer.late_fees} late fees, which is within the allowed limit.")
            return None
        # self.add_customer
        
        # for customer in self.customers: # loop through customers list
        #     if self.add_customer: # .library_card == library_card:
        #         customer_found = True
        
    
    # idk figure it out, there is something wrong with the file reader stuff
    def checkout_book(self, book_title, my_customer, checkedout_book):
        global checkout_date, due_date, book_info
        print(f"Do you have a library card, {my_customer.name}?")
        if self.add_customer(my_customer):
            checkout_date = datetime.today()
            self.due_date = checkout_date + timedelta(days=15)

            book_info = {
                'name': my_customer.name,
                'book_title': book_title,
                'checkout_date': checkout_date,
                'due_date': self.due_date,
                # 'available_copies': checkedout_book.copies
            }

            print(f"Librian is processing book, potential check book information: {book_info}")

        if book_title not in self.checkedout_books_on_file:
            self.checkedout_books_on_file[book_title] = [book_info]
            checkedout_book.copies -= 1

            if checkedout_book.copies <= 0:
                print(f"Sorry, no available copies of {book_title}")
                checkedout_book.add_to_waitlist(my_customer, checkedout_book)
                return None
        else:
            self.checkedout_books_on_file[book_title].append(book_info)
        # don't change anything above this comment
        if book_title in self.books_on_file:
            file_name = 'librarycopy.txt'
            with open(file_name, 'r') as file:
                for line in file:
                    parts = line.strip().split(', ')
                    book_title = parts[1]
                    new_copies = int(parts[3])
                    self.checkedout_books_on_file.append(book_title)
                    self.copies.append(new_copies)
        print(f"{my_customer.name} has checked out {book_title} on {checkout_date}. Book is due on {self.due_date}")
        return checkout_date, self.due_date, book_title



    def return_book(self, book_title, book):
        if book_title in self.checkedout_books_on_file:
            get_checkout_date = self.checkedout_books_on_file[book_title][-1]['checkout_date']
            if get_checkout_date:
                end = get_checkout_date + timedelta(days=45)
                self.return_date = get_checkout_date + (end - get_checkout_date) * random.random()
                print(f"Return date for {book_title} is {self.return_date}")
                self.calculate_late_fees(book_title)
                book.copies += 1

        return self.return_date
    
    def calculate_late_fees(self, book_title):
        # if 
        # #"using checkout_book method to find due date for book"
        # due_date = date.today() + timedelta(days = 14)

        # #"return_date is calculated the moment return_book method called since calculate_late_fees is calculated inside return_book
        # return_date = date.today()
    
        # #"to determine if returned before or after due date"
        # diff = return_date - due_date
    
        # #"if for returned before due date, else for returned after due date
        # if diff <= 0:
        #     return 0
        # else:
        #     fee = diff * 0.05
        #     return fee
        #     print("The late fee for {book_title} is ${fee}.")
    

        if __name__ == "__main__":
            library = Library()
            library.checkout_book("The Great Gatsby", "John Doe")
    