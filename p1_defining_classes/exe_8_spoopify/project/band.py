# from PythonOOP.p1_defining_classes.exe_8_spoopify.project.album import Album
# from PythonOOP.p1_defining_classes.exe_8_spoopify.project.song import Song


class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):  # album: Album
        if album in self.albums:
            return f"Band {self.name} already has {album.username} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.username}."

    def remove_album(self, album_name: str):
        albums_list = [a for a in self.albums if a.username == album_name]
        if albums_list:
            album = albums_list[0]
            if album.published:
                return "Album has been published. It cannot be removed."
            if album not in self.albums:
                return f"Album {album.username} is not found."
            self.albums.remove(album)
            return f"Album {album.username} has been removed."

    def details(self):
        result = f"Band {self.name}\n"
        for album in self.albums:
            result += f"{album.details()}\n"
        return result


# song = Song("Running in the 90s", 3.45, False)
# print(song.get_info())
# album = Album("Initial D", song)
# second_song = Song("Around the World", 2.34, False)
# print(album.add_song(second_song))
# print(album.details())
# print(album.publish())
# band = Band("Manuel")
# print(band.add_album(album))
# print(band.remove_album("Initial D"))
# print(band.details())