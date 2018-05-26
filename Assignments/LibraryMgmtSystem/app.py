from coreLibMgmt import Library
from Customer import Customer
from CustomLogger import logger
if __name__ == '__main__':
    library = Library(["book1", "book2", "book3"])
    customer = Customer()
    try:
        while True:
            print("\n 1. Available Books \n 2. Request Book \n 3. Return Book \n 4. Exit")
            userChoice = int(input())
            if userChoice is 1:
                library.displayAvailableBooks()
            elif userChoice is 2:
                reqBook = customer.requestBook()
                library.lendBook(reqBook)
            elif userChoice is 3:
                retBook = customer.returnBook()
                library.addBook(retBook)
            elif userChoice is 4:
                logger.warning("exiting system")
                exit()
    except BaseException as e:
        logging.error("Invalid Entry : Traceback::\n\n {} \n\n".format(e))
        map().__eq__()
