def test_config():
    return True

def divide_a_number(num1,num2):

    result = 0

    if num2 != 0:
        num1 / num2 == result

    else:
        return "\nDivision by 0 not allowed!\n"

    return result


def multiple_2_numbers():
    
    num1 = input(" Enter a number: ")
    while num1.isalpha():
        num1 = input("Enter digit(s): ")

    num2 = input(" Enter a number: ")
    while num2.isalpha():
        num2 = input("Enter digit(s): ")

    out = float(num1)*float(num2)#you can only float(number) not a letter
    print(out)

def open_fake_file():

    try:
        file = open("file_name", "r")

        contents = file.read()

        print(contents)

    except IOError:
        print("\nxxxxxxxxxxxxxxxxxx File cannot be found! xxxxxxxxxxxxxxxxxx\n")



