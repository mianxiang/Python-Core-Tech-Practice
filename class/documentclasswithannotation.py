class Document():
    
    WELCOME_STR = 'Welcome! The context for this book is {}.'

    def __init__(self, title, author, context):
        print('init function called')
        self.title = title
        self.author = author
        self.__context = context
    
    @classmethod
    def create_empty_book(cls, title, author):
        return cls(title = title, author = author, context = '')

    def get_context_length(self):
        return len(self.__context)
    
    @staticmethod
    def get_welcome(context):
        return Document.WELCOME_STR.format(context)

empty_book = Document.create_empty_book('Great Wall', 'Zhang Ruizhe')
print(empty_book.get_context_length())
print(empty_book.get_welcome('Nothing in this book, it is an empty book'))

    

        