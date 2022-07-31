# Проверка на число

def checking_for_a_number(text):

    test = True
    is_minus = False
    while test:
        number = input(f'{text}')
        if number[0] == '-':
            is_minus = True
            number = number.replace('-', '')
        elif number.isdigit():
            number = int(number)
            if is_minus:
                number *= (-1)
            test = False
        elif number.isdecimal:
            number = float(number)
            if is_minus:
                number *= (-1)
            test = False
        else:
            print("Error, incorrect number!")
    return number

checking_for_a_number(-125)


# def is_number(str):
#     try:
#         float(str)
#         return True
#     except ValueError:
#         return False
# a = input('введите число: ')
# print(is_number(a))