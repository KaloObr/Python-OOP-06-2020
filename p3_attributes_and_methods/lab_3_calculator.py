class Calculator:
<<<<<<< HEAD
    @staticmethod
    def add(*args):
        result = 0
        for i in args:
            result += i
=======


    @staticmethod
    def add(*args):
        result = 0
        for x in args:
            result += x
>>>>>>> 9fdae89e3c2105fcbb3bcdb44ae1b440fe51fb76
        return result

    @staticmethod
    def multiply(*args):
        result = 1
<<<<<<< HEAD
        for i in args:
            result *= i
        return result


=======
        for x in args:
            result *= x
        return result

    @staticmethod
    def divide(*args):
        result = args[0]
        for x in args[1:]:
            result = result / x
        return result

    @staticmethod
    def subtract(*args):
        result = args[0]
        for x in args[1:]:
            result -= x
        return result


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
>>>>>>> 9fdae89e3c2105fcbb3bcdb44ae1b440fe51fb76
