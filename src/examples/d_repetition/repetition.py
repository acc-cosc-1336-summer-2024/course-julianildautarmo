def test_config():
    return True

'''#sum of powers(3) = 1**1 + 2**2 + 3**3 = 14
def sum_of_powers(num): #define program
    sum = 0 #set sum initial to 0
    i = 0 #set index initial to 0

    while(i <= num): #boolean expression
        sum = sum + i *i #new sum is last sum plus current one
        i += 1 #index moves up by 1

    return sum

def display_number_for(num):

    for x in range(1, num+1):
        print(x)

def sum_of_powers_for(num):
    sum = 0
    for y in range(0, num):
        sum = sum + (y+1)**2

    return sum'''

def while_nested_loop(num):
    i=0
    while(i<num):
        print("waiting for inner")
        j=0
        while(j<num):
            print("\t inner", str(j))
            j+=1
        i+=1