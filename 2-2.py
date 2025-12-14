# class definition
class Song():
    def __init__(self,performer,title,album,year):
        self.performer=performer
        self.title=title
        self.album=album
        self.year=year
    def __str__(self):
        return f'Performer: {self.performer}\nTitle: {self.title}\nAlbum: {self.album}'

# object creation
song1 = Song('ed sheeran', "hearts don't break around here", 'divide', 2017)
song2 = Song('queen', 'bohemian rhapsody', 'a night at the opera', 1975)

## object usage
print(song1)
print(song2)