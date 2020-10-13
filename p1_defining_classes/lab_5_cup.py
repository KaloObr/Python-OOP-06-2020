class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def can_fill(self, mililiters):
        return mililiters <= self.status()

    def fill(self, mililiters):
        if not self.can_fill(mililiters):
            return
        self.quantity += mililiters

    def status(self):
        return self.size - self.quantity


cup = Cup(100, 50)
cup.fill(50)
cup.fill(10)
print(cup.status())

cup = Cup(100, 50)
cup.fill(10)
cup.fill(50)
print(cup.status())

