# Program to store game scores in file


def game():
    return -9

score = game()
with open ('hiscore.txt') as f:
    hiscore = int(f.read())

if hiscore == "":
    with open('hiscore.txt', 'w') as f:
        f.write(str(score))
        
        
elif int(hiscore)<score:
    with open('hiscore.txt', 'w') as f:
        f.write(str(score))
        