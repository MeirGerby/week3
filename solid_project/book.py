class Book:
    """store the book data """
    def __init__(self, title, author, content):
        self.title = title
        self.author = author
        self.content = content

    def __str__(self):
        return (f'-----------\n'
                f'Title: {self.title}\n'
                f'Author: {self.author}\n'
                f'Content: {self.content}\n'
                f'-----------\n')
book = Book('Mouse', "Meir", "Nothing")
print(book)

class SaveBook:
    """write the book data into a file"""

    @staticmethod
    def save_to_file(file_name: Book):
        with open ("books.txt", 'a') as f:
            f.write(f'-----------\n'
                    f'{file_name.content}\n')

        with open("books.txt", 'r') as f:
            print(f'File Content.\n'
                  f'{f.read()}')

save_book = SaveBook()
save_book.save_to_file(book)


