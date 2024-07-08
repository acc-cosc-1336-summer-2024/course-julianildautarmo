def test_config():
    return True

def create_dic():
    list = [1,2,3,4,5]
    langs = {'C++':'1979','Java':'1992','Python':'1996','C#':'2001','list':list} #this is a dictionary where a term has a dedicated "defenition"
    print(langs)

    #print(langs['C++'])
    #print(langs['C#'])

#can use this for item IDing, a part # and then its part name

#you can also put a list within it
    #print(langs['list'])

    langs['color'] = 'green' #just added a new key
    langs["C++"] = '1978'

    #print(langs['color'])
    #print(langs['C++'])

    print(langs)
    #now we see an extra term in lang and C++'s value has changed by a year

    if 'color' in langs: #use if so no error is generated if color isnt in the dictionary
        del langs['color']#kick that homie out
                  
    print(langs)#damn look at that, you dont got it, now ya do, now ya dont

    langs['int'] = 200
    langs['float'] = 1.05
    langs['boolean'] = True

    print('\n',langs)
    #print(langs['float'])

def loop_thru_dic():
        langs = {'C++':'1979','Java':'1992','Python':'1996','C#':'2001'}
        
        #for i in langs:
            #print(i,langs[i])
        #for i in langs:
            #print(langs[i])

        for keys, values in langs.items():
            print(keys,values)

        
def base_and_bask():
     baseball = set(['John','Mark','Barry','Max'])
     basketball = set(['Greg','Sean','Mark','Max'])

     sports = baseball.union(basketball)
     both = baseball.intersection(basketball)
     only_base = baseball.difference(basketball)
     only_bask = basketball.difference(baseball)

     print('play either ',str(sports))
     print('play both',str(both))
     print('only baseball', str(only_base))
     print('only basketball', str(only_bask))