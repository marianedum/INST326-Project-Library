import unittest


class Book:
    def __init__(self, title, author, genre, copies):
        pass
    
    def add_to_waitlist(self, customer):
        if customer.library_card is not None:
            if customer not in self.wailist:
                if len(customer.waitlist_books) < 5:
                   self.waitlist.append(customer)
                   # customer.(waitlist list).append(customer)
                   print(f"{customer.first_name} added to waitlist for {self.title}")
                else:
                   print(f"{customer.first_name} is already on waitlist waiting for 5 books")
            else:
                print(f"{customer.first_name} is already on waitlist for {self.title}")
        else:
            print("Customer has no card on file")


    def remove_from_waitlist(self):
        if self.waitlist:
            removed_customer = self.waitlist.pop(0)
            #  removed_customer.(waitlist list).remove(self)
            print(f"{removed_customer.first_name} has been removed from waitlist for {self.title}")
            for c, customer in enumerate(self.waitlist, start=1):
                print(f"Moving {customer.first_name} up in the waitlist")
            return removed_customer
        else:
            print("Waitlist is empty")
            return None
    
    import random


class Customer:
    def __init__(self, first_name, last_name, email, phone):
        # Customer class initialization
        self.name = first_name + " " + last_name
        self.email = email
        self.phone = phone
        self.library_card = None # added library card attribute, and since no card initially, set to None
        self.books_on_waitlist = []
        self.late_fees = 0
customer1 = Customer("John", "Snow", "john.snow@example.com", "240-578-4567")

print("Customer Name:", customer1.name)
print("Customer Email:", customer1.email)
print("Customer Phone:", customer1.phone)
print("Library Card Number:", customer1.library_card)
print("Books on Waitlist:", customer1.books_on_waitlist)
print("Late Fees:", customer1.late_fees)


class Library:
    def __init__(self):
        self.customers = []
        
    def add_customer(self, customer):
        # method to add new customer to library
        new_customer = Customer(customer)
        new_library_card = "{:05d}".format(random.randint(10000, 99999))
        new_customer.library_card = new_library_card
        self.customers.append(new_customer)
        print(f"Customer added with library card number {new_customer.library_card}")

    
    def remove_customer(self, id): 
        for email, customer in self.customers.items():
            if customer['id'] == id:
                del self.customers[email]
                return True
            return False
    
    def checkout_book(self, book_title, customer_card):
        with open('library.txt', 'r') as file:
                books = file.readlines()
                books = [book.strip()for book in books]

        if book_title in books:
                return f"Book {book_title} checkout initiated for {customer_card} Please return the {book_title} in 14 days."
        else:
                return f"Book {book_title} not found in library."

    def return_book(self, book_title, customer_card):
        if book_title in self.checked_out_book:
                if self.checked_out_book[book_title] == customer.card:
                    del self.checked_out_book[book_title]
                    return f"Book {book_title} has been returned"
                else:
                    return f"This book was not checked out by {customer_card}"
        else:
            return f"This book is not checked out or was not checked out."
    
    def calculate_late_fees(self, book_title):
        pass
    
class Test(unittest.TestCase):
    def testOne(self):
        self.book = Book("Harry Potter Book One")
        self.customer1 = Customer("John", "Doe", "11122334", ["The Perks of Being a Wallflower", "1984"])
        self.customer2 = Customer("Jane", "Doe", None, ["The Fire Next Time"])

    def test_add_to_waitlist(self):
        self.book.add_to_waitlist(self.customer1) # Add a customer to the waitlist
        self.assertIn(self.customer1, self.book.waitlist) # Checks if customer is in the waitlist
        self.book.add_to_waitlist(self.customer1)  #Adds customer again, checking to find duplicates
        self.assertEqual(len(self.book.waitlist), 1)  # Checks to see if there is one person on the wailist
        self.book.add_to_waitlist(self.customer2)  #Adds another customer to the waitlist, they have no library card)
        self.assertNotIn(self.customer2, self.book.waitlist) # Ensures second customer is not in the waitlist

    def test_remove_from_waitlist(self):
        self.book.add_to_waitlist(self.customer1)
        removed_customer = self.book.remove_from_waitlist()
        self.assertEqual(removed_customer, self.customer1)
        self.assertNotIn(self.customer1, self.book.waitlist)
        self.assertIsNone(self.book.remove_from_waitlist())
    
    def test_add_customer(self):
        lib = Library()
        lib.add_customer("person", "email@example.com", "202-605-3500")
        
        assert len(lib.customers) == 1
        assert lib.customers[1]["name"] == "person"
        assert lib.customers[1]["email"] == "email@example.com"
        assert lib.customers[1]["phone"] == "202-606-3500"
 
if __name__ == "__main__":
    unittest.main()
    