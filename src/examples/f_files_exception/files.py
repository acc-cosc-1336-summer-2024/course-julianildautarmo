def employee_filing(file):
    file = open(file, 'w')

    c = '1'

    while c == '1':
        id = input("Enter ID #: ")
        name = input("Enter Name: ")
        dept = input("Enter Dept: ")

        file.write(id+'\t')
        file.write(name+'\t')
        file.write(dept+'\n')

        c = input('Enter 1 to continue/Enter 2 to submit: ')

    file.close()

def read_records(file):
    file = open(file,"r")

    for line in file:
        record = line.split('\t')
        id = record[0]
        name = record[1]
        dept = record[2]

        print(id,name,dept)

    file.close()