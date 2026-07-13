import random
def play_game():
    youdict = {"s": 1, "w": -1, "g": 0}
    reverseddict = {1: "Snake", -1: "Water", 0: "Gun"}
    wins, loses, draws = 0, 0, 0

    print("==== Snake Water Gun ===")
    print("s = Snake | w = Water | g = Gun | q = Quit")

    while True:
        yourstr = input("\nChoose : ").lower().strip()

        if yourstr == "q":
            print(f"\nFinal score -> Wins: {wins} loses: {loses} Draw: {draws}")
            break

        if yourstr not in youdict:
            print("Invalid! Sirf s,w, ya g likho.")
            continue
        
        you = youdict[yourstr]
        computer = random.choice([1, -1, 0])

        print(f"Tum: {reverseddict[you]} | Computer: {reverseddict[computer]}")

        if computer == you:
            print("Draw!")
            draws += 1

        elif (computer == -1 and you == 0) or (computer == 1 and you == -1) or (computer == 0 and you == 1):
            print("Tum haare! ")
            loses += 1

        else:
            print("Tum jeete!")
            wins += 1
        
        print(f"Score -> W: {wins} L:{loses} D:{draws}")

play_game()
