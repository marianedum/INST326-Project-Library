class Book:
    def __init__(self, title, author, genre, copies):
        pass
    
    def add_to_waitlist(self, customer):
        pass
    
    def remove_from_waitlist(self):
        pass;
    
class Customer:
    def __init__(self, first_name, last_name, library_card):
        pass y;
    
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
            if customer['id'] == id:
                del self.customers[email]
                return True
            return False
    
    def checkout_book(self, book_title, customer_card):
        pass
    

    def return_book(self, book_title, customer_card):
        pass
    
    def calculate_late_fees(self, book_title):
        pass
    
    
if __name__ == "__main__":
    pass