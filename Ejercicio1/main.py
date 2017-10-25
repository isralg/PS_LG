import utils


def process_numbers(num_list):
    perfect_num_list = []
    defective_num_list = []
    abundant_num_list = []

    for num in num_list:
        if utils.is_perfect(num):
            perfect_num_list.append(num)
        if utils.is_defective(num):
            defective_num_list.append(num)
        if utils.is_abundant(num):
            abundant_num_list.append(num)

    print ("Perfect num list")
    print perfect_num_list
    print ("Defective num list")
    print defective_num_list
    print ("Abundant num list")
    print abundant_num_list
    print ("--------------------")
    print ("Finish process data")
    print ("--------------------")

def check_number(num):

    if utils.is_perfect(num):
        print ("Is a perfect number")
    if utils.is_defective(num):
        print ("Is a defective number")
    if utils.is_abundant(num):
        print ("Is a abundant number")

# --------- OPTION 1 --------- #
data = [12, 18, 20, 24, 30, 36, 6, 153, 14, 199, 251, 83, 28, 496, 8128]

# --------- OPTION 2 --------- #
# data = input("Introduzca una lista de numeros: ")

# --------- OPTION 3 --------- #
# start = input("Introduce un numero para iniciar rango: ")
# if not isinstance(start, int):
#     print("Wrong input data")
#     exit()
# end = input("Introduce un numero para terminar rango: ")
# if not isinstance(end, int):
#     print("Wrong input data")
#     exit()
#
# r = range(start, end)
# data = list(r)

if isinstance(data, int):
    check_number(data)
    exit()

if not isinstance(data, (list, tuple)):
    print ("Wrong input data, is not a list int numbers")
    exit()

process_numbers(data)
