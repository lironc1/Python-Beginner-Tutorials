print("Hi there, you are welcome to choose a game")
print("Press 1-3 to choose a game, press 4 to exit\n")

game1 = "1. AutoDraw"
game2 = "2. AutoRace"
game3 = "3. ManualRace"
Exit = "4. Exit"

print(game1 + "\n" + game2 + "\n" + game3 + "\n" + Exit)

userChoise = int(input())

print("\nYou chose option: ")

if userChoise == 1:
    print(game1)

if userChoise == 2:
    print(game2)

if userChoise == 3:
    print(game3)

if userChoise == 4:
    print(Exit)
