# build-in Functions for accessing attributes
# getattr() - __getattr__
# hasattr() - __hasatr__
# setattr() - __setattr__
# delattr() - __delattr__


class Employee:
    name = 'Harsh'
    salary = "25000"

    def show(self):
        print(self.name)
        print(self.salary)


employee = Employee()

# print(getattr(employee, 'name'))  # Harsh
# print(hasattr(employee, 'title'))  # False
# setattr(employee, "Money", "poor")
# print(getattr(employee, "Money"))
# delattr(employee, 'salary')
# these build in functions are dinamic. We can call them within any object with any key


# STATIC AND CLASS METHODS
# =======================================


# STATICK METHOD
class Computer:
    def __init__(self, cpu, ram_in_gb):
        if Computer.is_valid_ram(ram_in_gb):
            raise ValueError('Invalid RAM')
        self.cpu = cpu
        self.ram_in_gb = ram_in_gb

    @staticmethod      # Statick methods dont get self and dont have access to the state of our object
    def is_valid_ram(ram_in_gb):
        return ram_in_gb >= 0
    # Static method is a method that knows nothing about the class or instance it is called on
    # Works like a normal function outside of the class.
    # Bit dangerous tho, and its nice to limit their usability in the code.
    # dangerous because if one thing is statis it is difficult to change/substitue it
    # They are mostly used for utilities stuff

# PC = Computer("AMD", 16)


class MathUtils:
    current_result = 0

    @staticmethod
    def add(value):
        MathUtils.current_result += value

    @staticmethod
    def get_result():
        return MathUtils.current_result


MathUtils.add(5)
print(MathUtils.get_result())
MathUtils.add(3)
print(MathUtils.get_result())


# CLAS METHODS
# a class method is a method that gets passed the class it was called on (or instance)

class Cpu:
    def __init__(self, manufacturer, model, number_of_cores):
        self.manufacturer = manufacturer
        self.model = model
        self.number_of_cores = number_of_cores


class Computer2:
    def __init__(self, cpu, ram_in_gb):
        self.cpu = cpu
        self.ram_in_gb = ram_in_gb

    def get_details(self):
        return f'{self.cpu.number_of_cores}-core processor'

    @staticmethod
    def is_valid_ram(ram_in_gb):
        return ram_in_gb >= 0

    @classmethod
    def from_string(cls, computer_string):
        # {cpu_manufacturer};{cpu_model};{cpu_number_of_cores};{ram_in_gb}
        print('--- FROM classmethod ---')
        print(cls.__dict__)
        (cpu_manufacturer, cpu_model, cpu_number_of_cores, ram_in_gb) = computer_string.split(';')
        cpu = Cpu(cpu_manufacturer, cpu_model, cpu_number_of_cores)
        return cls(cpu, int(ram_in_gb))
        # The classmethod has access to the state of the class
        # This is useful when you want the method to be a factory for the class
        # Class methods are more commonly used because in Python there is no method overloading


def print_attribues(obj, offset=''):
    for key in obj.__dict__.keys():
        value = getattr(obj, key)
        if isinstance(value, int) or isinstance(value, str):
            print(f"{offset}{key}={value}")
        else:
            print(f'{offset}{key}')
            print_attribues(value, offset + ' ')


rog2 = Computer2.from_string('AMD;Ryzen 5 2600;6;8')
print_attribues(rog2)

