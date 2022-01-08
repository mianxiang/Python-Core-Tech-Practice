class Entity():
    def __init__(self, object_type):
        print('parent class init called')
        self.object_type = object_type
    
    def get_context_length(self):
        raise Exception('get_context_length not implemented')
    
    def print_title(self):
        print(self.title)

class Document(Entity):
    def __init__(self, title, author, context):
        print('Document class init called')
        super().__init__('Document')
        self.title = title
        self.author = author
        self.__context = context
    
    def get_context_length(self):
        return len(self.__context)

class Video(Entity):
    def __init__(self, title, author, video_length):
        print('Video class init called')
        super().__init__('Video')
        self.title = title
        self.author = author
        self.__video_length = video_length

    def get_context_length(self):
        return self.__video_length


harry_potter_book = Document('Harry Potter(book)', 'J K Rowling', 'It is a great story, so exciting.')
harry_potter_video = Video('Harry Potter(Video)', 'J K Rowling', 120)

print(harry_potter_book.object_type)
print(harry_potter_video.object_type)

harry_potter_book.print_title()
harry_potter_video.print_title()

print(harry_potter_book.get_context_length())
print(harry_potter_video.get_context_length())
