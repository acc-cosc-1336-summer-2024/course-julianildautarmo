def get_factorial(num):

    factorial = 1 #initialize output variable

    if(num >= 0): #setup case for valid positive inputs
        for i in range(1,num + 1): #create for loop that begins at 1 and ends at num+1 so last value is num
            factorial *= i 
            
        return factorial

    else:
        print("Negative numbers don't have factorials.")

        factorial = "NOT REAL"

        return factorial

def option_1_hw3():
    out = 0

    num = int(input("\nPick a number (1-10) and I'll give you the value of its factorial:\n"))
    if(1 <= num <= 10):

        out = get_factorial(num)

        print("\nThe factorial of", num, "is", out,"\n")
    else:
        option_1_hw3()
    
    option_3_hw_3()

def sum_odd_numbers(num):

    net_sum = 0
    current_num = 1

    while current_num <= num: #until they are equal and you add the input value
        net_sum += current_num #add each consecutive current_number
        current_num += 2 # +2 to stay with odd numbers only

    return net_sum

def option_2_hw_3():

    num = int(input("\nPick a number and I'll add up the odd numbers up to it (including it if its odd):\n"))
    if(1 <= num <=99):

        out = sum_odd_numbers(num)

        print("\nThe sum of all of the odd numbers up to",num, "is", out,"\n")
    else:
        print("Pick a number between 0 and 100\n")
        option_2_hw_3()
    
    option_3_hw_3()

def option_3_hw_3():
    exit_choice = 0
    exit_choice = input("Do you want to exit the program? (yes/no):")
    if(exit_choice == "yes"):
        print("Bye")

    else:
        print("Returning to the menu.")
        menu_all()

####################################################################################################################################################################

def menu_all():
        print("\nHomework 3 Menu\n-----------------------------------------------------")
        print("1- Factorial")
        print("2- Sum Odd Numbers")
        print("3- Exit")
        
        user_option = input("Please select an option:\n")
        
        if(user_option == "1"):
            option_1_hw3()

        elif user_option == "2":
            option_2_hw_3()

        elif user_option == "3":
            option_3_hw_3()

        else:
            print("\nPlease select a valid number input.")
            menu_all()
