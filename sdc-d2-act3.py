from random import randint

winning_numbers = str(randint(100, 999))

while True:
    player_bet = input("Enter a 3-digit number: ")
    if player_bet.isdigit() and len(player_bet) == 3:
        break
    else:
        print("Please enter a valid 3-digit number.")

print(f"Winning numbers are: {winning_numbers}")

if player_bet == winning_numbers:
    print("Congratulations! You won!")
elif sorted(player_bet) == sorted(winning_numbers):
    print("Congratulations! You partially won!")
else:
    print("Sorry, You lose!")