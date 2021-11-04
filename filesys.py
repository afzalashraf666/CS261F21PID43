import pandas as pd
from SongClass import Song


def store_csv(
    song_names, artist_names, plays, likes, comments, release_dates, reposts, genre_tags
):
    dataset = [
        song_names,
        artist_names,
        plays,
        likes,
        comments,
        release_dates,
        reposts,
        genre_tags,
    ]
    df = pd.DataFrame(data=dataset).T
    df.columns = [
        "NAME",
        "ARTIST",
        "VIEWS",
        "LIKES",
        "COMMENTS",
        "REL_DATE",
        "REPOSTS",
        "GENRE_TAG",
    ]
    df.to_csv("Scrapped30K.csv", index=False)


def read_csv():

    all_songs = []

    # reading csv file
    df = pd.read_csv("Scrapped30K.csv")
    # storing in lists
    song_names = df.NAME.values.tolist()
    artist_names = df.ARTIST.values.tolist()
    plays = df.VIEWS.values.tolist()
    likes = df.LIKES.values.tolist()
    comments = df.COMMENTS.values.tolist()
    release_dates = df.REL_DATE.values.tolist()
    reposts = df.REPOSTS.values.tolist()
    genre_tags = df.GENRE_TAG.values.tolist()

    # return song_names, artist_names, plays, likes, comments, release_dates, reposts, genre_tags
    for idx in range(0, len(song_names)):
        newSong = Song(
            song_names[idx],
            artist_names[idx],
            plays[idx],
            likes[idx],
            comments[idx],
            release_dates[idx],
            reposts[idx],
            genre_tags[idx],
        )
        all_songs.append(newSong)
    print("Length:", len(all_songs))
    return all_songs


def get_dataframe():
    df = pd.read_csv("Scrapped30K.csv")
    print(df)


if __name__ == "__main__":
    get_dataframe()
