class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.album = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photo_count):
        return cls(photo_count // 4)

    def add_photo(self, label):
        
        pass

    def display(self):
        return self.album



ph = PhotoAlbum(4)
print(ph.display())
