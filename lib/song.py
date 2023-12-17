class Song:
   count = 0  # Class attribute to keep track of the number of songs
   genres = []  # Class attribute to store unique genres
   artists = []  # Class attribute to store unique artists
   genre_count = {}  # Class attribute to store the count of songs for each genre
   artist_count = {}  # Class attribute to store the count of songs for each artist

def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()  # Call the class method to increment the count
        Song.add_to_genres(genre)  # Call the class method to add the genre to the genres list
        Song.add_to_artists(artist)  # Call the class method to add the artist to the artists list
        Song.add_to_genre_count(genre)  # Call the class method to update the genre count
        Song.add_to_artist_count(artist)  # Call the class method to update the artist count

@classmethod
def add_song_to_count(cls):
        cls.count += 1  # Increment the count using the class method

@classmethod
def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)  # Add the genre to the genres list if it's not already present

@classmethod
def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)  # Add the artist to the artists list if it's not already present

@classmethod
def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

@classmethod
def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

# Example usage:
#song1 = Song("Song 1", "Artist 1", "Rap")
#song2 = Song("Song 2", "Artist 2", "Rock")
#song3 = Song("Song 3", "Artist 3", "Country")
#song4 = Song("Song 4", "Artist 1", "Rap")
#song5 = Song("Song 5", "Artist 2", "Country")
#song6 = Song("Song 6", "Artist 1", "Rap")

#print(Song.artist_count)
# Output: {'Artist 1': 3, 'Artist 2': 2, 'Artist 3': 1}


pass
