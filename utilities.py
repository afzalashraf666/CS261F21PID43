from FileSys import *


def nonetyper(nonetype_obj):
    if nonetype_obj is None:
        nonetype_obj = "NIL"
        return str(nonetype_obj)
    
    if type(nonetype_obj) is str:
        return str(nonetype_obj)
    else:
        return str(nonetype_obj.text)

def garbage_remover(garbage_string):
    if len(garbage_string) > 0:
        if garbage_string[0].isdigit():
            return garbage_string
        else:
            return "0"

def garbage_filter(garbage_string):

    garbage_string = str(garbage_string)
    if garbage_string[0].isdigit() and len(garbage_string) < 15 and len(garbage_string) > 0:
        string = (garbage_string).replace(',',"")
        string = string.strip()
        if string[-1] == "k" or string[-1] == "K":
            string = (garbage_string).replace("K","")
            string = (string).replace("k","")
            string_int = float(string) * 1000
            return int(string_int)

        elif string[-1] == "m" or string[-1] == "M":
            string = (garbage_string).replace('M',"")
            string = (string).replace('m',"")
            string_int = float(string) * 1000000
            return int(string_int)
        
        elif string[-1] == "b" or string[-1] == "B":
            string = (garbage_string).replace('B',"")
            string = (string).replace('b',"")
            string_int = float(string) * 1000000000
            return int(string_int)
        
        else:
            string_int = float(string)
            return int(string_int)
    
    else:
        return int(0)

def attribute_iterator(attribute_list):
    temp = []
    for attrib in attribute_list:
        temp.append(garbage_filter(attrib))
    return temp


if __name__ == "__main__":
    
    song_names, artist_names, plays, likes, comments, release_dates, reposts, genre_tags = read_csv()
    comments = attribute_iterator(comments)
    likes = attribute_iterator(likes)
    plays = attribute_iterator(plays)
    reposts = attribute_iterator(reposts)
    store_csv(song_names, artist_names, plays, likes, comments, release_dates, reposts, genre_tags)