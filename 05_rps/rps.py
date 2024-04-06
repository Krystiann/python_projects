from random import choice
import sys

class RPS:
    def __init__(self):
        print('Welcom in RPS GAME !')

        self.moves = {'rock':'🪨', 'paper':'📰', 'scissors':'✂'}
        self.valid_moves = list(self.moves.keys())

    def play_game(self):
        user_move =  input(f'Rock, Paper or Scissors? (exit) >> ').lower()
        if user_move == 'exit':
            print(f'Thanks for playing')
            sys.exit()

        if user_move not in self.valid_moves:
            print(f'Invalid move, please input correct move (rock/paper/scissors)')
            return self.play_game()

        ai_move = choice(self.valid_moves)

        self.display_moves(user_move, ai_move)
        self.check_moves(user_move, ai_move)


    def display_moves(self, user_move, ai_move):
        print('-'*20)
        print(f'You : {self.moves[user_move]}')
        print(f'AI : {self.moves[ai_move]}')
        print('-' * 20)

    def check_moves(self, user_move, ai_move):
        if user_move == ai_move:
            print(f'It is a tie !')
        elif user_move == 'rock' and ai_move == 'scissors':
            print(f'You win !')
        elif user_move == 'scissors' and ai_move == 'paper':
            print(f'You win!')
        elif user_move == 'paper' and ai_move == 'rcok':
            print(f'You win !')
        else:
            print(f'AI win !')



if __name__=='__main__':
    rps = RPS()

    while True:
        rps.play_game()
