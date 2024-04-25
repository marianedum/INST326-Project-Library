import sys


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