from P4_Python_OOP.p4_encapsulation.exe_1_wild_cat_zoo.project.caretaker import Caretaker
from P4_Python_OOP.p4_encapsulation.exe_1_wild_cat_zoo.project.cheetah import Cheetah
from P4_Python_OOP.p4_encapsulation.exe_1_wild_cat_zoo.project.keeper import Keeper
from P4_Python_OOP.p4_encapsulation.exe_1_wild_cat_zoo.project.lion import Lion
from P4_Python_OOP.p4_encapsulation.exe_1_wild_cat_zoo.project.tiget import Tiger
from P4_Python_OOP.p4_encapsulation.exe_1_wild_cat_zoo.project.vet import Vet


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.animals = []
        self.workers = []

        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity


    def add_animal(self, animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.username} the {animal.__class__.__name__} added to the zoo"

        elif self.__budget < price:
            return f"Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.username} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"


    def fire_worker(self, worker_name):
        for employee in self.workers:

            if employee.username == worker_name:
                self.workers.remove(employee)

                return f"{employee.username} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        amount_to_pay = sum([employee.salary for employee in self.workers])

        if self.__budget >= amount_to_pay:
            self.__budget -= amount_to_pay
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        animal_care_cost = sum([animal.get_needs() for animal in self.animals])

        if self.__budget >= animal_care_cost:
            self.__budget -= animal_care_cost
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    @staticmethod
    def get_individual_element_in_collection(collection, name):
        result = f'----- {len(collection)} {name}:\n'
        result += "\n".join([str(i) for i in collection])
        return result

    def animals_status(self):
        lions = [a for a in self.animals if a.__class__.__name__ == "Lion"]
        tigers = [a for a in self.animals if a.__class__.__name__ == "Tiger"]
        cheetahs = [a for a in self.animals if a.__class__.__name__ == "Cheetah"]

        result = f'You have {len(self.animals)} animals\n'
        result += self.get_individual_element_in_collection(lions, 'Lions') + '\n'
        result += self.get_individual_element_in_collection(tigers, "Tigers") + '\n'
        result += self.get_individual_element_in_collection(cheetahs, "Cheetahs")

        return result

    def workers_status(self):
        keepers = [p for p in self.workers if p.__class__.__name__ == 'Keeper']
        caretakers = [p for p in self.workers if p.__class__.__name__ == 'Caretaker']
        vets = [p for p in self.workers if p.__class__.__name__ == 'Vet']

        result = f'You have {len(self.workers)} workers\n'
        result += self.get_individual_element_in_collection(keepers, "Keepers") + '\n'
        result += self.get_individual_element_in_collection(caretakers, "Caretakers") + '\n'
        result += self.get_individual_element_in_collection(vets, "Vets")

        return result



zoo = Zoo("Zootopia", 3000, 5, 8)

# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))

# Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Fireing worker
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())
