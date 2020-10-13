# from PythonOOP.p1_defining_classes.exe_7_guild_system.project.player import Player
# from PythonOOP.p1_defining_classes.exe_7_guild_system.project.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player.guild == "Unaffiliated":
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.username} to the guild {self.name}"
        elif player.guild != self.name:
            return f"Player {player.username} is in another guild."
        else:
            return f"Player {player.username} is already in the guild."

    def kick_player(self, player_name):
        for member in self.players:
            if player_name == member.username:
                self.players.remove(member)
                member.guild = "Unaffiliated"  # MIGHT BLOW
                return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = f"Guild: {self.name}\n"

        for member in self.players:
            result += member.player_info()

        return result

#
# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
# guild = Guild("UGT")
# print(guild.assign_player(player))
# print(guild.guild_info())
