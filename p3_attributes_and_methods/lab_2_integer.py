class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, value):
        return Integer(int(value))

    @classmethod
    def from_roman(cls):
        pass

    @classmethod
    def from_string(cls, value):
        return Integer(int(value))

    def add(self, integer):
        return self.value + integer



 