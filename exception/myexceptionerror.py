class MyInputError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self) -> str:
        return("{} is invalid input".format(repr(self.value)))

if __name__ == "__main__":
    try:
        raise MyInputError(1)
    except MyInputError as err:
        print("error:{}".format(err))
