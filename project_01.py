import random
# Snake Water  Gun or Rock paper scissor 
def gamewin(comp,you):
# If two values are equal, declare a tie!
    if comp == you:
        return None
 # Check for all possibilities when computer chose s
    elif  comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
 # Check for all possibilities when computer chose w   
    elif comp=='w':
        if you=='g':
            return False
    elif you =='s':
        return True
 # Check for all possibilities when computer chose g
    elif comp=='g':
        if you=='s':
            return False
        elif you== 'w':
            return True
        
print("computer turn:Snake(s) Water(w) or Gun(g)?")
randNo=random.randint(1,3)
if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'
elif randNo==3:
    comp='g'
you=input("your turn:Snake(s) Water(w) or Gun(g)\n")
a=gamewin(comp,you)
print(f"computer choce {comp} ")
print(f"you choce {you} ")
if a==None:
    print("game is tai!")
elif a:
    print("you Win!")
else:
    print("you loss!")