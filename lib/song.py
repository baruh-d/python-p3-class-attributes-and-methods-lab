class Song:

    count =0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self,name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        self.add_to_genres(self.genre)
        self.add_to_artists(self.artist)
        

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls):
        cls.genre_count ={}
        for genre in cls.genres:
            count = sum(1 for song in cls.all_songs() if song.genre == genre)
            cls.genre_count[genre] = count

    @classmethod
    def add_to_artist_count(cls): 
        cls.artist_count ={}
        for artist in cls.artists:
            count = sum(1 for song in cls.all_songs() if song.artist == artist)
            cls.artist_count[artist] = count

    @classmethod
    def all_songs(cls): 
        return [song for song in cls.__subclasses__()]
    
song1 = Song("Song 1", "Artist 1", "Pop")
song2 = Song("Song 2", "Artist 2", "Rock")
print(Song.count)