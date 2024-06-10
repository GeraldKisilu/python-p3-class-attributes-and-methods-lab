class Song:
    count = 0
    genre_count = {}
    artist_count = {}
    genres = set()
    artists = set()

    def __init__(self, title, artist, genre):
        self.title = title
        self.artist = artist
        self.genre = genre
        
        # Update the song count
        Song.count += 1
        
        # Update the genre count
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1
            Song.genres.add(genre)
        
        # Update the artist count
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1
            Song.artists.add(artist)
