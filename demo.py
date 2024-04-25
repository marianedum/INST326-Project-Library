import sys

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
    
class Customer:
    def __init__(self, first_name, last_name, library_card):
        pass
    
class Library:
    def __init__(self):
            self.customers = {}
            self.next_id = 1

    def add_customer(self, name, email, phone):
        self.next_id += 1
        id = self.next_id

        customer = {
            "id": id, 
            "name": name,
            "email": email,
            "phone": phone
        }  

        self.customers[id] = customer

    
    def remove_customer(self, id): 
        for email, customer in self.customers.items():
            if customer['id'] ==. id:
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
    
    
if __name__ == "__main__":
    pass