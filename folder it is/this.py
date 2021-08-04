def game():
    return 64

score= game()
with open('0myscore.txt') as f:
    hiscore= f.read()
    
if hiscore=='' :
    with open('0myscore.txt', 'w') as f:
        f.write(str(score))
        
elif int(hiscore)<score :
    with open('0myscore.txt', 'w') as f:
        f.write(str(score))