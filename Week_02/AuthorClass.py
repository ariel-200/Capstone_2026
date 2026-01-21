# Author Class
class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

# Publish Method - add book title to the book list if it's not already in the list
    def publish(self, title):
        if title not in self.books:
            self.books.append(title)
        else: # Else - print an error message
            print('Error: Title already exists')

# String Method
    def __str__(self):
        # Join the book list to 1 string if the list is not empty
        # Or print 'No books'
        book_list = ', '.join(self.books) or 'No books'
        return f"Author: {self.name}. Books Published: {book_list}"

# Main Method
def main():
    seuss = Author('Dr. Seuss')
    seuss.publish('The Cat in the Hat')
    seuss.publish('Hop on Pop')
    seuss.publish('The Cat in the Hat')
    print(seuss)
    me = Author('Ariel B')
    print(me)

main()
