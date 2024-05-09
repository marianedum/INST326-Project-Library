import unittest
from datetime import datetime, timedelta
import random

class Book:
    def __init__(self, book_title, author, copies):
        self.book_title = book_title
        self.author = author
        self.copies = copies
        self.waitlist = []

        
    
    def add_to_waitlist(self, customer):
        # if condition for check out -- if book has already been checkout
        library = Library()
        book = Book ()
        my_customer = Customer ()
        if library.checkout_book:
        # call to see if book is in wailist
            if customer.library_card is not None:
                if customer not in self.wailist:
                    if len(customer.waitlist_books) < 5:
                        self.waitlist.append(customer)
                        print(f"{customer.first_name} added to waitlist for {self.book_title}")
                        return self.waitlist                 
                    else:
                        print(f"{customer.first_name} is already on waitlist waiting for 5 books")
                        return None
                else:
                    print(f"{customer.first_name} is already on waitlist for {self.book_title}")
                    return None
            else:
                print("Customer has no card on file")
                return None
        return None


    def remove_from_waitlist(self):
        if self.waitlist:
            removed_customer = self.waitlist.pop(0)
            customer_removed = Customer()
            customer_removed.books_on_waitlist.remove(self.book_title)
            print(f"{removed_customer.first_name} has been removed from waitlist for {self.book_title}")
            for c, customer in enumerate(self.waitlist, start=1):
                print(f"Moving {customer.first_name} up in the waitlist")
            return removed_customer
        else:
            print("Waitlist is empty")
            return None
            
class Customer:
    def __init__(self, first_name, last_name, email, phone):
        self.name = first_name + " " + last_name
        self.email = email
        self.phone = phone
        self.library_card = None 
        self.books_on_waitlist = []
        self.late_fees = 0
       
class Library:
    def __init__(self):
            self.customers = {}
            self.checked_out_books_on_file = {}
            self.copies = {}

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
            return 
        else:
            print(f"Customer with library card {customer.library_card} has {customer.late_fees} late fees, which is within the allowed limit.")
            return
                       
        if not customer_found:
            print(f"No customer found with library card {library_card}")
        try: 
            library_card = int(library_card)
        except ValueError:
            print(f"Invalid library card number {library_card}")
            self.customers.remove(customer)
            return customer_name
        finally:
            return None
        # self.add_customer
        
        # for customer in self.customers: # loop through customers list
        #     if self.add_customer: # .library_card == library_card:
        #         customer_found = True
        
    
    def checkout_book(self, book_title, customer):
        if not self.copies:
            file_name = 'library.txt'
            with open(file_name, 'r') as file:
                for line in file:
                    parts = line.strip().split(', ')
                    title = parts[1]
                    copies = int(parts[3])
                    self.copies[title] = copies

        if book_title not in self.copies or self.copies[book_title] == 0:
            print("Sorry, no available copies of", book_title)
            return None

        checkout_date = datetime.today()
        due_date = checkout_date + timedelta(days=30)

        book_info = {
            'name': customer,
            'checkout_date': checkout_date,
            'due_date': due_date
        }

        if book_title not in self.checked_out_books_on_file:
            self.checked_out_books_on_file[book_title] = [book_info]
        else:
            self.checked_out_books_on_file[book_title].append(book_info)
            self.copies[book_title] -= 1
            if self.copies[book_title] == 0:
                print(f"Sorry, no available copies of {book_title}")
                return None

        return checkout_date, due_date



    def return_book(self, book_title, customer):
        if book_title in self.checked_out_books_on_file:
            customer = Customer()
            checkout_date = self.checkout_date
            for c in customer.customers:
                if customer.library_card:
                    del self.checked_out_book_on_file[book_title]
                    end = checkout_date + timedelta(days = 30)
                    for i in range(30):
                        random_return_date = checkout_date + (end - checkout_date) * random.random()
                        print(random_return_date)

                        # days_checked_out = (return_date - checkout_date).days
                        # late_fee = self.calculate_late_fees()
                        return random_return_date
                else:
                    return None
            return None
    
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
    
# class Test(unittest.TestCase):
#     def testOne(self):
#         self.book = Book("Harry Potter Book One")
#         self.customer1 = Customer("John", "Doe", "11122334", ["The Perks of Being a Wallflower", "1984"])
#         self.customer2 = Customer("Jane", "Doe", None, ["The Fire Next Time"])

#     def test_add_to_waitlist(self):
#         self.book.add_to_waitlist(self.customer1) # Add a customer to the waitlist
#         self.assertIn(self.customer1, self.book.waitlist) # Checks if customer is in the waitlist
#         self.book.add_to_waitlist(self.customer1)  #Adds customer again, checking to find duplicates
#         self.assertEqual(len(self.book.waitlist), 1)  # Checks to see if there is one person on the wailist
#         self.book.add_to_waitlist(self.customer2)  #Adds another customer to the waitlist, they have no library card)
#         self.assertNotIn(self.customer2, self.book.waitlist) # Ensures second customer is not in the waitlist

#     def test_remove_from_waitlist(self):
#         self.book.add_to_waitlist(self.customer1)
#         removed_customer = self.book.remove_from_waitlist()
#         self.assertEqual(removed_customer, self.customer1)
#         self.assertNotIn(self.customer1, self.book.waitlist)
#         self.assertIsNone(self.book.remove_from_waitlist())
        
#     def test_checkout_book(self):
#         self.book.checkout_book(self.book, self.customer1)
#         self.assertIn(self.checkout)
#         self.book.checkout_book(self.customer1)
#         self.assertIn(self.customer1)
           
#     def test_return_book(self):
#       self.book.checkout_book(self.book, self.customer1)
#       return_book = self.book.return_book, self.customer1.return_book
#       self.assertEqual(return_book, self.book, self.customer1)
#       self.assertIsNone(self.book.return_book())

class TestCheckoutBook(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.customer = Customer("John Doe", "johndoe@example.com", "1234567890")
        self.library.add_customer(self.customer)
        self.library.copies["The Great Gatsby"] = 1

    def test_checkout_valid_book(self):
        checkout_date, due_date = self.library.checkout_book("The Great Gatsby", self.customer)
        self.assertIsNotNone(checkout_date)
        self.assertIsNotNone(due_date)
        self.assertEqual(self.library.copies["The Great Gatsby"], 0)

    def test_checkout_invalid_book(self):
        checkout_date, due_date = self.library.checkout_book("The Catcher in the Rye", self.customer)
        self.assertIsNone(checkout_date)
        self.assertIsNone(due_date)

    def test_checkout_out_of_stock(self):
        self.library.checkout_book("The Great Gatsby", self.customer)
        checkout_date, due_date = self.library.checkout_book("The Great Gatsby", self.customer)
        self.assertIsNone(checkout_date)
        self.assertIsNone(due_date)

if __name__ == "__main__":
    unittest.main()
 
# if __name__ == "__main__":
    
#     library = Library()
#     library.checkout_book("The Great Gatsby", "John Doe")
    