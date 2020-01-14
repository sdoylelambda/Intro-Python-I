# ROCK PAPER SCISSORS GAME
import random

# start of helper function
# def process_choices(player_move, cpu_move):
#     if player_move == cpu_move:
#         print("Tie")
#         return 0
#     elif player_move == 'r' and

# REPL
wins = 0
losses = 0
ties = 0

choices = ['r', 'p', 's']

# LOOP
while True:
    # READ
    cmd = input("->")
    cpu_move = random.choice(choices)
    # EVAL
    if cmd == 'r':
        if cpu_move == 'r':
            print("Tie")
            ties += 1
        elif cpu_move == "p":
            print("Lose")
            losses += 1
        elif cpu_move == 's':
            print("Win")
            wins += 1

    elif cmd == 'p':
        if cpu_move == 'r':
            print("Win")
            wins += 1
        elif cpu_move == "p":
            print("Tie")
            ties += 1
        elif cpu_move == 's':
            print("Lose")
            losses += 1

    elif cmd == 's':
        if cpu_move == 'r':
            print("Lose")
            losses += 1
        elif cpu_move == "p":
            print("Win")
            wins += 1
        elif cpu_move == 's':
            print("Tie")
            ties += 1

    elif cmd == 'q':
        # Quit
        print("Goodbye")
        break
    else:
    # PRINT
        print("I did not recognize that command")
    print(f"Score: {wins} /{losses} / {ties}")
