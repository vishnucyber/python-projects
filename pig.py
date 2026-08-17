import random
def roll():
    roll = random.randint(1,6)
    return roll

while True:
    players = input("Enter the no of players(2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4")
    else:
        print("Invalid ,try again.")

max_score = 50
player_score = [0 for _ in range(players)]

while max(player_score ) < max_score:
    for player_idx in range(players):
        print(f"\n Player {player_idx + 1} has just started ")
        print(f"Your total score is {player_score[player_idx]}\n")
        current_score = 0

        while True:   
            should_roll = input("Would you want to roll (y)? ").lower()
            if should_roll != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled the one.! Turn done")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled {value}")

            

            print(f"your score is {current_score} ")

        player_score[player_idx] += current_score
        print(f"Your total score is: {player_score[player_idx]}")

max_score = max(player_score)
winning_indx = player_score.index(max_score)
print(f"Player number {winning_indx + 1} has won ")