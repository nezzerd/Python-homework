import random


class MusicAlbum:
    def __init__(self, title, artist, country, release_year, genre, tracklist):
        self.title = title
        self.artist = artist
        self.country = country
        self.release_year = release_year
        self.genre = genre
        self.tracklist = tracklist

    def info(self):
        print(f"Album Title: {self.title}")
        print(f"Artist: {self.artist}")
        print(f"Country: {self.country}")
        print(f"Release Year: {self.release_year}")
        print(f"Genre: {self.genre}")
        print("Tracklist:")
        for track in self.tracklist:
            print(track)

    def play_track(self, track_number):
        print(f"Now playing: {self.tracklist[track_number - 1]}")

    def play_random_track(self):
        random_track = random.choice(self.tracklist)
        print(f"Now playing: {random_track}")


album = MusicAlbum(
    title="Nevermind",
    artist="Nirvana",
    country="USA",
    release_year=1991,
    genre="Rock",
    tracklist=["Smells Like Teen Spirit", "Come As You Are", "Lithium"]
)

album.info()
album.play_track(2)
album.play_random_track()
