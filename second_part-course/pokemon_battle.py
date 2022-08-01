from random import randint
# Pokémon battle made on python


def enter_continue():
    input('Press ENTER to continue>')


def attack_cpu(attack_chosen, life_player):  # Function to choose the CPU attack
    if attack_chosen == 1:
        # Do attack_1
        attack_1 = 'Tail volt'
        print('Pikachu has used {}'.format(attack_1))

        print('You lose 10 life points')
        life_player -= 10
        return life_player

    elif attack_chosen == 2:
        # Do attack _2
        attack_2 = 'Thunder'
        print('Pikachu has used {}'.format(attack_2))

        print('You lose 11 life points')
        life_player -= 11
        return life_player


def attack_player(life_cpu):  # Function to choose the player attack
    user_attack_chosen = None

    attack_player_1 = 'Tackle'
    attack_player_2 = 'Water gun'
    attack_player_3 = 'Bubble'

    while user_attack_chosen != 1 and user_attack_chosen != 2 and user_attack_chosen != 3:
        user_attack_chosen = ('Chose an attack:\n 1. {}\n 2. {}\n 3.{}\n>'
                              .format(attack_player_1, attack_player_2, attack_player_3))

        if user_attack_chosen == '1':
            # Do attack_player_1 ("Tackle")
            print('Squirtle has used {}'.format(attack_player_1))

            print('Pikachu lose 10 life points')
            life_cpu -= 10
            return life_cpu

        elif user_attack_chosen == '2':
            # Do attack_player_2 ("Water gun")
            print('Squirtle has used {}'.format(attack_player_2))

            print('Pikachu lose 12 life points')
            life_cpu -= 12
            return life_cpu

        elif user_attack_chosen == '3':
            # Do attack_player_3 ("Bubble")
            print('Squirtle has used {}'.format(attack_player_3))

            print('Pikachu lose 9 life points')
            life_cpu -= 9
            return life_cpu


def show_life(life_pokemon_player, life_pokemon_cpu):
    print('Pikachu´s life points: {}'.format(life_pokemon_cpu))
    print('(You) Squirtle´s life points: {}'.format(life_pokemon_player))


def battle_run(life_pokemon_player, life_pokemon_cpu):  # While to run the battle until one die
    print('Battle with wild Pikachu!!')
    enter_continue()

    while life_pokemon_player > 0 and life_pokemon_cpu > 0:
        show_life(life_pokemon_player, life_pokemon_cpu)
        enter_continue()

        attack_cpu_chosen = randint(1, 2)
        attack_cpu(attack_cpu_chosen, life_pokemon_player)

        enter_continue()  # Next turn
        show_life(life_pokemon_player, life_pokemon_cpu)
        enter_continue()

        attack_player(life_pokemon_cpu)
        enter_continue()


if __name__ == '__main__':
    life_pikachu = 80
    life_squirtle = 75

    battle_run(life_squirtle, life_pikachu)
