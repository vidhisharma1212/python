import random 

def game(computer,you):
    if computer=='s' and you=='w':
        return False
    elif computer=='s' and you=='g':
        return True
    elif computer=='s' and you=='s':
        return None
    elif computer=='w' and you=='g':
        return False
    elif computer=='w' and you=='s':
        return True
    elif computer=='w' and you=='w':
        return None
    elif computer=='g' and you=='s':
        return False
    elif computer=='g' and you=='w':
        return True
    elif computer=='g' and you=='g':
        return None
    

e= random.randint(1,3)
# print(e)
if e==1:
    computer= 's'
elif e==2:
    computer= 'w'
elif e==3:
    computer= 'g'
print("Computer: Snake(s) , Water(w) or Gun(g) ")

you = input("Player : Snake(s) , Water(w) or Gun(g) ? : ")

print(f"Computer chose {computer}")
print(f"You chose {you}")

x= game(computer, you)
if x==True: 
    print("You won!")
elif x==False: 
    print("You lost!")
else: 
    print("Game is tie ! ")