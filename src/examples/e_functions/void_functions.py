#

'''
num1=100 #global num1
num2=200 #global num2

def local_variables(num1,num2):
    var1=5
    var2="python"

    print("")
    print(num1,num2,var1,var2)
    print("")

def local_variables_value_return1(num1,num2):
    numx = num1+num2
    print("")
    print("Value Return Function...\t",numx)
    print("")
    print(num1,num2, "local") #here num1 and num2 values are within a certain section only

def local_variables_value_return2(num3,num4):
    numy = num3+num4
    print("")
    print("value returned, not printed")
    print("")
    return numy

def main():
    local_variables(1,2) #local num1 and num2 WITHIN "main" function ONLY
    local_variables_value_return1(3,4)
    local_variables_value_return2(5,6)    
    

main() # I have 3 functions above all seperately created, then called together via main function

print(num1,num2, "global") # here we see global variables being printed even when they locally were changed (within "local_variables_value_return1" function)
'''

