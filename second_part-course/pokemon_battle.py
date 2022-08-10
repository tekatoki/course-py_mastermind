from random import randint
import os
# Pokémon battle made on python


def clear():
    if os.name == 'posix':
        os.system('clear')

    elif os.name == 'ce' or os.name == 'nt' or os.name == 'dos':
        os.system('cls')

    else:
        os.system('clear')


def show_life(life_pokemon_player, life_pokemon_cpu):
    if life_pokemon_player < 0:
        life_pokemon_player = 0

    elif life_pokemon_cpu < 0:
        life_pokemon_cpu = 0

    progress_bar_life_player = int(life_pokemon_player * 10 / LIFE_SQUIRTLE)
    progress_bar_life_cpu = int(life_pokemon_cpu * 10 / LIFE_PIKACHU)

    print('Squirtle:  [{}{}] ({}/{}) life points'
          .format('#' * progress_bar_life_player, ' ' *
                  (10 - progress_bar_life_player), life_pokemon_player, LIFE_SQUIRTLE))
    print('Pikachu:  [{}{}] ({}/{}) life points'
          .format('#' * progress_bar_life_cpu, ' ' * (10 - progress_bar_life_cpu), life_pokemon_cpu, LIFE_PIKACHU))


def enter_continue():
    input('Press ENTER to continue>')
    clear()


def checks_pokemon_die(life_pokemon_player, life_pokemon_cpu):
    if life_pokemon_player <= 0:
        show_life(life_pokemon_player, life_pokemon_cpu)
        print('You lose the battle!! :(')
        input('The battle is over>')
        exit()

    elif life_pokemon_cpu <= 0:
        show_life(life_pokemon_player, life_pokemon_cpu)
        print('You win the battle!! :)')
        input('The battle is over>')
        exit()


def battle_run(life_pokemon_player, life_pokemon_cpu):  # While to run the battle until one die
    print('Battle with wild Pikachu!!')
    enter_continue()

    while life_pokemon_player > 0 and life_pokemon_cpu > 0:
        print("Pikachu's turn!!")
        enter_continue()

        attack_pikachu = randint(1, 2)

        if attack_pikachu == 1:
            # Do attack_1
            attack_1 = 'Tail volt'
            print('Pikachu has used {}'.format(attack_1))

            print('You lose 10 life points')
            life_pokemon_player -= 10

        elif attack_pikachu == 2:
            # Do attack_2
            attack_2 = 'Thunder'
            print('Pikachu has used {}'.format(attack_2))

            print('You lose 11 life points')
            life_pokemon_player -= 11

        enter_continue()

        checks_pokemon_die(life_pokemon_player, life_pokemon_cpu)

        show_life(life_pokemon_player, life_pokemon_cpu)
        enter_continue()

        print('Your turn!!')
        enter_continue()

        attack_player_1 = 'Tackle'
        attack_player_2 = 'Water gun'
        attack_player_3 = 'Bubble'

        user_attack_chosen = input('Chose an attack:\n 1. {}\n 2. {}\n 3.{}\n>'
                                   .format(attack_player_1, attack_player_2, attack_player_3))

        if user_attack_chosen == '1':
            # Do attack_player_1 ("Tackle")
            print('Squirtle has used {}'.format(attack_player_1))
            print('Pikachu lose 10 life points')
            life_pokemon_cpu -= 10

        elif user_attack_chosen == '2':
            # Do attack_player_2 ("Water gun")
            print('Squirtle has used {}'.format(attack_player_2))

            print('Pikachu lose 12 life points')
            life_pokemon_cpu -= 12

        elif user_attack_chosen == '3':
            # Do attack_player_3 ("Bubble")
            print('Squirtle has used {}'.format(attack_player_3))

            print('Pikachu lose 9 life points')
            life_pokemon_cpu -= 9

        else:
            print('Please, insert a valid option [1, 2, 3]')
            enter_continue()

        # If any pokemon died continue:

        show_life(life_pokemon_player, life_pokemon_cpu)
        enter_continue()

    # When you win the battle (because the while exit when the cpu die)

    show_life(life_pokemon_player, life_pokemon_cpu)
    print('You win the battle!! :)')
    input('The battle is over>')


if __name__ == '__main__':
    LIFE_PIKACHU = 80
    LIFE_SQUIRTLE = 85

    battle_run(LIFE_SQUIRTLE, LIFE_PIKACHU)
