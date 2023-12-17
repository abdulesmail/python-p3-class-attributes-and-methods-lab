#!/usr/bin/env python3

from song import Song


class TestSong:
    '''Class "Song" in song.py'''

    def test_saves_name_artist_genre(self):
        '''instantiates with a name, artist, and genre.'''
        out_of_touch = Song("Out of Touch", "Hall and Oates", "Pop")
        assert out_of_touch.name == "Out of Touch"
        assert out_of_touch.artist == "Hall and Oates"
        assert out_of_touch.genre == "Pop"

    def test_has_song_count(self):
        '''counts the total number of Song objects.'''
        # Reset the count for each test
        Song.count = 0

        assert Song.count == 0
        Song("99 Problems", "Jay Z", "Rap")
        Song("Halo", "Beyonce", "Pop")
        Song("Smells Like Teen Spirit", "Nirvana", "Rock")
        assert Song.count == 3
        Song("Sara Smile", "Hall and Oates", "Pop")
        assert Song.count == 4

    def test_has_genres(self):
        '''keeps track of all Song genres.'''
        # Reset the genres for each test
        Song.genres = []

        assert "Rap" not in Song.genres
        assert "Pop" not in Song.genres
        assert "Rock" not in Song.genres

        Song("99 Problems", "Jay Z", "Rap")
        Song("Halo", "Beyonce", "Pop")
        Song("Smells Like Teen Spirit", "Nirvana", "Rock")

        assert "Rap" in Song.genres
        assert "Pop" in Song.genres
        assert "Rock" in Song.genres

    def test_has_artists(self):
        '''keeps track of all Song artists.'''
        # Reset the artists for each test
        Song.artists = []

        assert "Jay Z" not in Song.artists
        assert "Beyonce" not in Song.artists
        assert "Hall and Oates" not in Song.artists

        Song("99 Problems", "Jay Z", "Rap")
        Song("Halo", "Beyonce", "Pop")
        Song("Sara Smile", "Hall and Oates", "Pop")

        assert "Jay Z" in Song.artists
        assert "Beyonce" in Song.artists
        assert "Hall and Oates" in Song.artists
        
    def test_has_genre_count(self):
        '''keeps count of Songs for each genre.'''
        # Reset the genre_count for each test
        Song.genre_count = {}

        assert Song.genre_count.get("Rap", 0) == 0
        assert Song.genre_count.get("Pop", 0) == 0
        assert Song.genre_count.get("Rock", 0) == 0

        Song("99 Problems", "Jay Z", "Rap")
        Song("Halo", "Beyonce", "Pop")
        Song("Smells Like Teen Spirit", "Nirvana", "Rock")

        assert Song.genre_count.get("Rap", 0) == 1
        assert Song.genre_count.get("Pop", 0) == 1
        assert Song.genre_count.get("Rock", 0) == 1

    def test_has_artist_count(self):
        '''keeps count of Songs for each artist.'''
        # Reset the artist_count for each test
        Song.artist_count = {}

        assert Song.artist_count.get("Jay Z", 0) == 0
        assert Song.artist_count.get("Beyonce", 0) == 0
        assert Song.artist_count.get("Nirvana", 0) == 0
        assert Song.artist_count.get("Hall and Oates", 0) == 0

        Song("99 Problems", "Jay Z", "Rap")
        Song("Halo", "Beyonce", "Pop")
        Song("Smells Like Teen Spirit", "Nirvana", "Rock")
        Song("Sara Smile", "Hall and Oates", "Pop")

        assert Song.artist_count.get("Jay Z", 0) == 1
        assert Song.artist_count.get("Beyonce", 0) == 1
        assert Song.artist_count.get("Nirvana", 0) == 1
        assert Song.artist_count.get("Hall and Oates", 0) == 2
