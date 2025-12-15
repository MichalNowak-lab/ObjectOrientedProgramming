class Ebook:
    def __init__(self,title,author,number_of_pages):
        self.title = title
        self.author = author
        self.number_of_pages=number_of_pages
        self.current_page=1
        self.book_open = False
    def open(self):
        self.book_open=True
    def close(self):
        self.book_open = False
    def next_page(self):
        if self.current_page<self.number_of_pages and self.book_open:
            self.current_page+=1
        else:
            print('Not possible, book is closed')
    def prev_page(self):
        if self.current_page>1 and self.book_open:
            self.current_page-=1
        else:
            print('Not possible, book is closed')
    def status(self):
        print(f'Title: {self.title}, Author: {self.author}, Page numbers: {self.number_of_pages}, Current Page: {self.current_page}')
