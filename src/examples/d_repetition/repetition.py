def test_config():
    return True

#sum of powers(3) = 1**1 + 2**2 + 3**3 = 14
def sum_of_powers(num): #define program
    sum = 0 #set sum initial to 0
    i = 0 #set index initial to 0

    while(i <= num): #boolean expression
        sum = sum + i *i #new sum is last sum plus current one
        i += 1 #index moves up by 1

    return sum