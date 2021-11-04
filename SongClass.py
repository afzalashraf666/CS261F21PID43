class Song:
    all_attributes = []
    def __init__(self, song_name, artist_name, plays, likes, comments, release_date, reposts, genre_tags):
        self.all_attributes = [str(song_name), str(song_name), str(artist_name), int(plays), int(likes), int(comments), int(reposts), int(release_date), str(genre_tags)]