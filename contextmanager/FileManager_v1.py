class FileManager:
    def __init__(self, name, mode):
        print('calling __init__ method')
        self.name = name
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        print('calling __enter__ method')
        self.file = open(self.name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('calling __exit__ method')
        if self.file:
            self.file.close()
        if exc_type:
            print(f'exc_type:{exc_type}')
            print(f'exc_value:{exc_val}')
            print(f'exc_traceback:{exc_tb}')
        return True

with FileManager('test.txt', 'w') as f:
    f.write('hello world')
    raise Exception('exception raised').with_traceback(None)
    

