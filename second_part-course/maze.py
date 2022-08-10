import random
import msvcrt
import os

# Program that creates a little terminal game like Rogue


def clear():
    if os.name == 'posix':
        os.system('clear')

    elif os.name == 'ce' or os.name == 'nt' or os.name == 'dos':
        os.system('cls')

    else:
        os.system('clear')


def random_items(parameter_array, number_iterates, parameter_map_width, parameter_map_height):
    # Function that creates a number of items in an array that you insert as a parameter
    i = 0
    while i < number_iterates:
        parameter_array.append([random.randint(0, parameter_map_width), random.randint(0, parameter_map_height)])
        # This random.randint creates the automatically a coordinate X and Y
        i += 1


def print_map(parameter_map_width_x, parameter_map_height_y, parameter_player_coordinate, parameter_objects):
    # The parameter_player_coordinate must be an array with two ints
    # The parameter_objects must be an array as well

    # Checks if the player is in the limit of the map
    # If the player is in the limit of the map, it will appear on the other side of the map

    # For the coordinate x
    parameter_player_coordinate[0] %= parameter_map_width_x

    # For the coordinate y
    parameter_player_coordinate[1] %= parameter_map_height_y

    print('+' + '-' * parameter_map_width_x * 3 + '+')

    for coordinate_y in range(parameter_map_height_y):
        print('|', end='')
        for coordinate_x in range(parameter_map_width_x):
            symbol_print = ' '

            for object_array in parameter_objects:  # Prints the objects
                if object_array[0] == coordinate_x and object_array[1] == coordinate_y:
                    symbol_print = '*'

                elif object_array[0] == parameter_player_coordinate[0]\
                        and object_array[1] == parameter_player_coordinate[1]:
                    parameter_objects.remove(object_array)

            if parameter_player_coordinate[1] == coordinate_y and parameter_player_coordinate[0] == coordinate_x:
                symbol_print = '@'

            print(' {} '.format(symbol_print), end='')
        print('|')

    print('+' + '-' * parameter_map_width_x * 3 + '+')


def main_program():
    # Main constants:

    # Map coordinates
    MAP_WIDTH_X = 20
    MAP_HEIGHT_Y = 15

    # Number of items
    NUMBER_ITEMS = 10

    # [Position_X, Position_Y]

    # Coordinates of the player
    player_position = [3, 1]

    # Create coordinates of the map's items
    map_items = []
    random_items(map_items, NUMBER_ITEMS, MAP_WIDTH_X, MAP_HEIGHT_Y)

    # Show the map for first time
    print_map(MAP_WIDTH_X, MAP_HEIGHT_Y, player_position, map_items)

    # The var to store the direction of the player
    direction = ''

    while direction not in ['Q', 'q']:
        print('WASD to move [Q to exit]>')
        direction = msvcrt.getwch()

        # If you insert wasd the player will move
        if direction in ['W', 'w']:
            player_position[1] -= 1
        elif direction in ['S', 's']:
            player_position[1] += 1
        elif direction in ['A', 'a']:
            player_position[0] -= 1
        elif direction in ['D', 'd']:
            player_position[0] += 1

        # Otherwise, if you do not insert any valid option the player will not do anything
        elif direction not in ['Q', 'q', 'W', 'w', 'S', 's', 'A', 'a', 'D', 'd']:
            pass

        clear()
        print_map(MAP_WIDTH_X, MAP_HEIGHT_Y, player_position, map_items)


if __name__ == '__main__':
    main_program()
