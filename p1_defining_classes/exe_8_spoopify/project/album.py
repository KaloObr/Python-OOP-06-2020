# from PythonOOP.p1_defining_classes.exe_8_spoopify.project.song import Song


class Album:
    def __init__(self, name, songs=None):
        self.name = name

        if songs is None:
            self.songs = []
        elif not isinstance(songs, list):
            self.songs = []
            self.songs.append(songs)
        else:
            self.songs = songs

        self.published = False

    def add_song(self, song):  # song: Song
        if song.single:
            return f"Cannot add {song.username}. It's a single"
        if self.published:
            return f"Cannot add songs. Album is published."
        if song in self.songs:
            return f"Song is already in the album."
        self.songs.append(song)
        return f"Song {song.username} has been added to the album {self.name}."

    def remove_song(self, song_name):
        if song_name not in [song.username for song in self.songs]:
            return "Song is not in the album."
        if self.published:
            return "Cannot remove songs. Album is published."
        song = [s for s in self.songs if s.username == song_name][0]
        # list(filter(lambda x: x.name == song_name, self.songs))[0]
        self.songs.remove(song)
        return f"Removed song {song.username} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = f"Album {self.name}\n"
        for song in self.songs:
            result += f"== {song.get_info()}\n"
        return result
