def test_config():
    return True



def loop_string_while():
    y = "Python"
    i = 0

    while(i < len(y)):
        print(y[i])
        i += 1


def loop_string_for_unfixed():
    p = "coffees"
    indx=0

    while(indx < (len(p))):
        print(p[indx])
        indx += 1

def loop_string_for_fixed():
    p = "coffees"
    indx=0

    for indx in range(0,6): #this guy works the same when a word has only 6 letters, but after this, its over since the values are only going to be printed if len <=6, it'll get cut off
        print(p[indx])
        indx += 1

def loop_string_for_fixed_edited():
    p = "coffees"
    indx=0

    for indx in range(0,len(p)): 
        print(p[indx])