import random

def game():
    score = random.randint(1, 100)
    print("You are Playing....")

    with open("Hiscore.txt") as f:
        hiscore = f.read()
        print(f"High score is: {hiscore}")
    if hiscore != "":
        hiscore = int(hiscore)

    else:
        hiscore = 0

    print(f"Your score is : {score}")
    
    if score > hiscore:
        with open("Hiscore.txt", "w") as f:
            f.write(str(score))
        print("Congrass..! Hit the Highscore...")
    return score

game()

