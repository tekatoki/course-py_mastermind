# Test code to learn how to do a while

def user_option():

    def valid_option():
        print('Valid option')

    user_input = None

    while user_input != 'A' and user_input != 'B' and user_input != 'C':

        user_input = input('Choose a option [A, B, C]>')

        if user_input == 'A':
            valid_option()
        elif user_input == 'B':
            valid_option()
        elif user_input == 'C':
            valid_option()


if __name__ == '__main__':
    user_option()
