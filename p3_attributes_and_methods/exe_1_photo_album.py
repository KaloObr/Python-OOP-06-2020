class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [] # <- MATRIX the amount of sublists must be equel to the number of pages
        self.page = 0

        for num in range(self.pages):
            self.photos.append([])

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(photos_count // 4)

    def add_photo(self, label):
        try:
            if len(self.photos[self.page]) == 4:
                self.page += 1
        except:
            return "No more free slots"
        if self.page >= self.pages:
            return "No more free slots"
        self.photos[self.page].append(label)
        return f"{label} photo added successfully on page " \
               f"{self.page + 1} slot {len(self.photos[self.page])}"

    def display(self):
        result = ''
        for page in self.photos:
            result += '-' * 11 + "\n"
            for photo in page:
                result += '[] '
            result += '\n'
        result += '-'*11
        return result


album = PhotoAlbum(10)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.add_photo("wedding"))
print(album.add_photo("wedding"))
print(album.add_photo("wedding"))
print(album.display())


#print(album.display())


