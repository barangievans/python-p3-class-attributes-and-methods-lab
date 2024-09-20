class Song:
    count = 0
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        Song.count += 1
        Song.genre_count[genre] = Song.genre_count.get(genre, 0) + 1
        Song.artist_count[artist] = Song.artist_count.get(artist, 0) + 1
        
        # Optional: To keep track of unique genres and artists
        if 'genres' not in Song.__dict__:
            Song.genres = set()
        if 'artists' not in Song.__dict__:
            Song.artists = set()
        
        Song.genres.add(genre)
        Song.artists.add(artist)
