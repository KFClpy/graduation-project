class WrongPassword(Exception):
    def __int__(self, value):
        self.value = value

    def __repr__(self):
        repr(self.value)
