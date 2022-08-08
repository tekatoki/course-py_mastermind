import os
# A terminal program that saves the items you want to buy in an array


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


def shop_list_program(parameter_array):
    while True:
        show_array(parameter_array)

        user_input = input('What would you like to buy [Q to exit]> ')
        clear()

        if user_input in ['Q', 'q']:
            show_array(parameter_array)
            break

        elif user_input not in ['Q', 'q']:

            if user_input in parameter_array:
                input('You have already {} save in your list [ENTER to continue]> ')
                clear()

            else:
                confirmation_input = []

                while confirmation_input not in ['Y', 'y', 'N', 'n']:
                    confirmation_input = input('Are you sure you would like to add {} in your list [Y/N]> '
                                               .format(user_input))
                    clear()

                    if confirmation_input in ['Y', 'y']:
                        input('{} has been added to your list [ENTER to continue]> '.format(user_input))
                        clear()

                        parameter_array.append(user_input)

                    elif confirmation_input in ['N', 'n']:
                        input('{} has not been added to your list [ENTER to continue]> '.format(user_input))
                        clear()


if __name__ == '__main__':
    array = []
    shop_list_program(array)
