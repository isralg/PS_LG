import utils

# list = list(input("Introduzca una lista de numeros: "))
list = [12, 18, 20, 24, 30, 36, 6, 153, 14, 199, 251, 83, 28, 496, 8128]

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
    print ("He terminado de procesar la lista de numeros")

process_numbers(list)
