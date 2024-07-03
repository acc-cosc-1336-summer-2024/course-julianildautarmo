####################################################################################################################################################################

def menu():
        print("\nHomework 5 Menu\n-----------------------------------------------------")
        print("1- Hamming Distance")
        print("2- DNA Complement")
        print("3- Exit")
        
        user_option = input("Please select an option:\n")
        
        if(user_option == "1"):
            option_1()

        elif user_option == "2":
            option_2()

        elif user_option == "3":
            option_3()

        else:
            print("\nPlease select a valid number input.")
            menu()
            
############################################################

def get_hamming_distance(dna1,dna2):
    d = 0
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            d+=1
    
    return d

def option_1():

    dna1 = input('\nGive me the 1st dna sequence (Only give in form "AGCT"\n\n).')
    dna2 = input('\nGive me the 2nd dna sequence (Only give in form "AGCT"\n\n).')

    out = 0
    out = str(get_hamming_distance(dna1,dna2))

    print("\nThe Hamming Distance of ", dna1, "and", dna2, "is ", out, ".\n")
    
    option_3()

def get_dna_complement(dna):

    dna = str(dna)#make sure its a string
    temp_dna = dna[::-1]#reverse the input dna string
    
    complement_dic = {'A':'T','T':'A','C':'G','G':'C'} #create a dictionary with each letters "anti-letter"
    
    complement_dna = '' #create an empty string to add into from dictionary values
    
    for i in (temp_dna):#go thru each letter, which is a key
        complement_dna += complement_dic.get(i,'')# and add the key's value to the string, since this will be user input we need to cover our butts if they input bad values (not dna)

    return complement_dna

def option_2():
    out = ""
    dna = input("\nGive me a dna strand and I'll provide it's complement\n")

    out = get_dna_complement(dna)

    print("\nThe complement of ", dna, " is ", out, ".\n")
    
    option_3()

def option_3():
    exit_choice = 0
    exit_choice = input("Do you want to exit the program? (yes/no):")
    if(exit_choice == "yes"):
        print("Bye")

    else:
        print("Returning to the menu.")
        menu()
