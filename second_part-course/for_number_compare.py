import os


def warning():
    print('WARNING: Do not inserted any character that is not a number.\n'
          'If you insert any character that is not a number the program will show an ERROR')
    input('Press ENTER to continue> ')
    clear()


def show_array(parameter_array):
    input('Your list:{} [Press ENTER to continue]> '.format(parameter_array))
    clear()


def clear():
    if os.name == 'posix':
        os.system('clear')

    elif os.name == 'ce' or os.name == 'nt' or os.name == 'dos':
        os.system('cls')

    else:
        os.system('clear')


def compare_numbers(parameter_array):
    greater_num = parameter_array[0]
    lower_num = parameter_array[0]

    for number in parameter_array:

        if number > greater_num:
            greater_num = number

        elif number < lower_num:
            lower_num = number

        else:
            pass

    input('The lowest number is: {}\n'
          'The greatest number is: {}\n'
          .format(lower_num, greater_num))


def main_program(parameter_array):
    warning()
    while True:
        show_array(parameter_array)

        user_input = input('What would you like to add to the list [Q to exit]> ')
        clear()

        if user_input in ['Q', 'q']:
            show_array(parameter_array)
            break

        elif user_input not in ['Q', 'q']:
            user_input = int(user_input)
            parameter_array.append(user_input)

    compare_numbers(parameter_array)


if __name__ == '__main__':
    array_numbers = []
    main_program(array_numbers)
