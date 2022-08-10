import os
# This code will show you how many blank spaces, dots and commas has a phrase that you had insert on the console


def clear():
    if os.name == 'posix':
        os.system('clear')

    elif os.name == 'ce' or os.name == 'nt' or os.name == 'dos':
        os.system('cls')

    else:
        os.system('clear')


def program():
    phrase = input('Insert your phrase> ')
    clear()

    white_spaces = 0
    commas = 0
    dots = 0

    for i in phrase:
        if i == ' ':
            white_spaces += 1

        elif i == ',':
            commas += 1

        elif i == '.':
            dots += 1

    print('Your phrase: {} has:\n'
          'blanks_spaces: {}\n'
          'commas: {}\n'
          'dots: {}\n'.format(phrase, white_spaces, commas, dots))


if __name__ == '__main__':
    program()
