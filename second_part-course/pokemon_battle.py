from random import randint
# Pokémon battle made on python


def show_life(life_pokemon_player, life_pokemon_cpu):
    print('Pikachu´s life points: {}'.format(life_pokemon_cpu))
    print('(You) Squirtle´s life points: {}'.format(life_pokemon_player))


def enter_continue():
    input('Press ENTER to continue>')


def checks_pokemon_die(life_pokemon_player, life_pokemon_cpu):
    if life_pokemon_player <= 0:
        print('You lose the battle!! :(')
        input('The battle is over>')
        exit()

    elif life_pokemon_cpu <= 0:
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

        checks_pokemon_die(life_pokemon_player, life_pokemon_cpu)
        # If any pokemon died continue:

        show_life(life_pokemon_player, life_pokemon_cpu)
        enter_continue()


if __name__ == '__main__':
    life_pikachu = 80
    life_squirtle = 75

    battle_run(life_squirtle, life_pikachu)
