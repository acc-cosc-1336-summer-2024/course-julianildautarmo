#


def get_p_distance(list1,list2):
    d = 0 #initialize variable d
    for i in range(len(list1)):
        if list1[i] != list2[i]:#go thru the lists and find hamming distance
            d+=1

    pd = d/len(list1)#hamming distance/total length
    return pd

def get_p_distance_matrix(list1):

    len_dna = len(list1)#get length of sequence
    
    matrix = [[0.00000]*len_dna for _ in range(len_dna)]#create matrix thats filled with zeros to be filled in

    for row_i in range(len_dna):#go down the list doing the below loop and you get a set of lets in a single list
        for col_j in range(len_dna):#go down the list doing the below action and you get a list 
            matrix[row_i][col_j] = get_p_distance(list1[row_i],list1[col_j])#matrix of this i and this j = pd or i and j

    return matrix


def matrix_operation(): #to actually show user the matrix

    list1 = input("\nInput a list of DNA strands in the format below:\n\n[[a,b,c],[d,e,f],[g,h,i]]\n\n")#get list1 which is a matrix (list with lists within)
    #list1 = [['T','T','T','C','C','A','T','T','T','A'],['G','A','T','T','C','A','T','T','T','C'],['T','T','T','C','C','A','T','T','T','T'],['G','T','T','C','C','A','T','T','T','A']]
    list1 = ["".join(sublist) for sublist in list1] #at every "" join the sublist so we can get a string of only letters

    matrix_to_print = get_p_distance_matrix(list1) #get matrix and give it name/variable

    for row in matrix_to_print:#print matrix for user
        print(" ".join(f"{x:.5f}" for x in row))#gives 5 decimal points


################################################################################################
def menu():
        print("\nHomework 6 Menu\n-----------------------------------------------------")
        print("1- Get P-Distance Matrix")
        print("2- Exit")
        
        user_option = input("Please select an option:\n")
        
        if(user_option == "1"):
            option_1()

        elif user_option == "2":
            option_2()

        else:
            print("\nPlease select a valid number input.")
            menu()




def option_1():

    matrix_operation()
    
    option_2()

def option_2():
    exit_choice = input("Do you want to exit the program? (yes/no):")
    if(exit_choice == "yes"):
        print("Bye")

    else:
        print("Returning to the menu.")
        menu()
