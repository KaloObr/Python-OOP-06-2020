# from PythonOOP.p1_defining_classes.exe_6_pokemon_battle.project.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon):
        if pokemon in self.pokemon:
            return "This pokemon is already caught"
        self.pokemon.append(pokemon)

        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name):
        for seperate_pokemon in self.pokemon:
            if pokemon_name == seperate_pokemon.username:
                self.pokemon.remove(seperate_pokemon)
                return f"You have released {pokemon_name}"

        return "Pokemon is not caught"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\n"\
                 f"Pokemon count {len(self.pokemon)}\n"
        for pkmn in self.pokemon:
            result += "- " + pkmn.pokemon_details() + "\n"

        return result


# pokemon = Pokemon("Pikachu", 90)
# print(pokemon.pokemon_details())
# trainer = Trainer("Ash")
# print(trainer.add_pokemon(pokemon))
# second_pokemon = Pokemon("Charizard", 110)
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.trainer_data())
