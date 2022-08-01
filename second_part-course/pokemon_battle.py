from random import randint


def battle_run(life_pokemon_player, life_pokemon_cpu):  # While to run the battle until one die
    print('Battle with wild Pikachu!!')
    input('Press ENTER to continue>')

    def attack_cpu(attack_chosen, life_player):
        if attack_chosen == 1:
            # Do attack_1
            attack_1 = 'Tail volt'
            print('Pikachu has used []'.format(attack_1))

            print('You lose 10 life points')
            life_player -= 10
            return life_player

        elif attack_chosen == 2:
            # Do attack _2
            attack_2 = 'Thunder'
            print('Pikachu has used []'.format(attack_2))

            print('You lose 11 life points')
            life_player -= 11
            return life_player

    while life_pokemon_player > 0 and life_pokemon_cpu > 0:

        attack_cpu_chosen = randint(1, 2)
        attack_cpu(attack_cpu_chosen, life_pokemon_player)

        input('Press ENTER to continue>')  # Next turn


if __name__ == '__main__':
    life_pikachu = 80
    life_squirtle = 75
