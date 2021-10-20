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