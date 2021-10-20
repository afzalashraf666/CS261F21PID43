import pandas as pd

def store_csv(song_names, artist_names, plays, likes, comments, release_dates, reposts, genre_tags):
    dataset = [song_names, artist_names, plays, likes, comments, release_dates, reposts, genre_tags]
    df = pd.DataFrame(data = dataset).T
    df.columns = ["NAME" , "ARTIST" , "VIEWS" , "LIKES" , "COMMENTS" , "REL. DATE" , "REPOSTS" , "GENRE TAG"]
    df.to_csv("datasets.csv" ,index=False)