def test_config():
    return True

def list_in_list():
    masterlist = [[1,2,3],[4,5,6],[7,8,9]]

    sublist1 = masterlist[0]
    sublist2 = masterlist[1]
    sublist3 = masterlist[2]

    print(sublist1)
    print(sublist2)    
    print(sublist3)

def x_matrix(rows,cols): #just tables in python, lists within lists. This allows us to have 2d lists AKA tables
    
    list = []

    for i in range(0,rows):
        row_list = []

        for j in range(0,cols):
            row_list.append((i+1)*(j+1))

            list.append(row_list)

    print(list)


def create_tuple(): #lists you cant change values of, very simple

    readonly_list = (1,2,3,4,5)

    print(readonly_list)
    print(readonly_list[0], readonly_list[1], readonly_list[2], readonly_list[3], readonly_list[4])

    if 5 in readonly_list:
        print("Yes")
    
    print(len(readonly_list))
