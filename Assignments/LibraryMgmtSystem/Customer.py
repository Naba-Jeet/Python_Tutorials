import logging

logging.basicConfig(filename='test.log', level=logging.DEBUG,
                    format='%(levelname)s:--:%(name)s:--:%(message)s:--:%(funcName)s:--:%(lineno)s:--%(asctime)s:')



class Customer:
    def requestBook(self):
        logging.info("request book")
        print("Enter name of Book : ")
        # Expression to check if requested book is available and than lend a book to the user
        
    def returnBook(self):
        logging.warning("returning book")
        print("Enter book to return")
        # Expression to return the book a user lended earlier
