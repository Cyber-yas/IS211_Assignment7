
import random

def roll_die():
    return random.randint(1, 6)

def play_game():
    score1, score2 = 0, 0
    current_player = 1

    
    while score1 < 100 and score2 < 100:
        turn_total = 0
        print(f"\nCurrent Scores - Player 1: {score1}, Player 2: {score2}")

        while True:
            roll = roll_die()
            print(f"Player {current_player} rolled a {roll}")

            if roll == 1:
                print("Oops! You rolled a 1. No points this turn.")
                turn_total = 0
                break

            else:
                turn_total += roll
                print(f"Turn total: {turn_total}")

                action = input("Do you want to roll again (r) or hold (h)? ").lower()
                if action == 'h':
                    if current_player == 1:
                        score1 += turn_total

                    else:
                        score2 += turn_total
                    print(f"Player {current_player}'s total score is now {score1 if current_player == 1 else score2}")
                    break
        
        current_player = 2 if current_player == 1 else 1  # Switch players

    print(f"\nPlayer {current_player} wins with a score of {score1 if current_player == 1 else score2}!")

if __name__ == "__main__":
    random.seed(0)  
    play_game()