
class MusicLibrary:
    def display_info(self):
        print("The following are the songs:")

class Song:
    def __init__(self, title, artist, album, duration):
        self.title = title
        self.artist = artist
        self.album = album
        self.duration = duration

    def displayinfo(self):
        print(f"{self.title} by {self.artist} ({self.album}) - {self.duration} seconds")

class Playlist(MusicLibrary):
    def __init__(self, title, description):
        super().__init__()  
        self.title = title
        self.description = description
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def display(self):
        print(f"Playlist: {self.title}\nDescription: {self.description}")
        print("Songs:")
        for song in self.songs:
            song.displayinfo()

class Library(MusicLibrary):
    def __init__(self):
        super().__init__() 
        self.playlists = []

    def add_playlist(self, playlist):
        self.playlists.append(playlist)

    def display(self):
        print("Library Playlists:")
        for playlist in self.playlists:
            playlist.display()

song1 = Song("2AM", "Talha yunus", "A tale of two Talhas", 240)
song2 = Song("KONG", "Faris Shafi", "No album", 190)
song3 = Song("Zindagi sy mout", "Talha Anjum", "No album", 122)

playlist1 = Playlist("RAP", "Paki rap")
playlist1.add_song(song1)
playlist1.add_song(song2)
playlist1.add_song(song3)

library = Library()
library.add_playlist(playlist1)
library.display()

