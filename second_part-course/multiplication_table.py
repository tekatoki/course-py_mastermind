import os
'''
This code shows all the multiplication table of a number that you insert on the console
Example: Insert a number> 2
1 x 2 = 2 
2 x 2 = 4
3 x 2 = 6
... # Until 10
'''


def clear():
    if os.name == 'posix':
        os.system('clear')

    elif os.name == 'ce' or os.name == 'nt' or os.name == 'dos':
        os.system('cls')

    else:
        os.system('clear')


def for_table(parameter_number):

    for number in range(1, 11):
        print('{} x {} = {}'.format(number, parameter_number, number * parameter_number))


def main_program():
    print('WARNING: Do not inserted any character that is not a number.\n'
          'If you insert any character that is not a number the program will show an ERROR')
    user_input = int(input('Insert a number> '))
    clear()

    for_table(user_input)


if __name__ == '__main__':
    main_program()
