
from classes import Player,Roll
import random


ROLLS = ['rock','scissors','paper']

def print_header():
    print('---------------------------------')
    print('          ROLL GAME!!!')
    print('---------------------------------')
    print()


def game_loop(player1, player2, rolls):
    count = 0
    while count < 3:
        print('{} vs {} ----> {}:{}'.format(player1.name,player2.name,player1.count,player2.count))
        p2_roll = Roll(random.choice(rolls)) # TODO: get random roll
        p1_roll = Roll(input('Please enter your roll [rock,scissors,paper]: ')) # TODO: have player choose a roll

        outcome = p1_roll.can_defeat(p2_roll)

        # display throws
        print('{} has {} and {} has {}'.format(player1.name,p1_roll.roll_type,player2.name,p2_roll.roll_type))
        # display winner for this round
        if outcome == 'win':
            print('the round winner is {}'.format(player1.name))
            player1.count+=1
        elif outcome == 'lose':
            print('the round winner is {}'.format(player2.name))
            player2.count+=1
        else: 
            print('DRAW!!!')
            player1.count+=1
            player2.count+=1

        count += 1
    if player1.count>player2.count:
        print("{} is a winner. The SCORE IS: ---{}:{}---".format(player1.name,player1.count,player2.count))
    elif player2.count<player2.count:
        print("{} is a winner. The SCORE IS: ---{}:{}---".format(player2.name,player1.count,player2.count))
    else:
        print('Nobody won, ITS a DRAW!!! The SCORE IS: ---{}:{}---'.format(player1.count,player2.count))
    # Compute who won


def get_players_name():
    name = input('Please print your name: ')
    return name

   
def build_the_three_rolls():
    result = []
    for roll in ROLLS:
        result.append(Roll(roll))
    

def main():
    print_header()

    rolls = build_the_three_rolls()

    name = get_players_name()

    player1 = Player(name)
    player2 = Player("computer")

    game_loop(player1, player2, ROLLS)


if __name__ == '__main__':
    main()
