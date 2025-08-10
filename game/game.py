#hello we are karen and kian peyrovan and this game is scissors, paper and rock

import random
import cowsay

def equal():
    cowsay.cow('your text is equal with ai')

def Win():
    cowsay.trex('you are winner this round')
def lose():
    cowsay.cow('ai is winner this round')

def m():
    cowsay.dragon('you are winner this game')
def k():
    cowsay.cow('ai is winner game')

y=input('1.play with ai or 2.play with friend:')
if y=="1" or y=="play with ai":

    
    l=int(input('number of play:'))
    r=l


    f='b'
    score1=0
    score=0

    
    while l!=0:


        l=l-1
        if f!='i':

            i=input('text:')
            o=random.choice(['scissors','rock','paper'])

        if i=='rock'and o=='scissors':
            print('ai text:',o)
            Win()
            score=score+1
            print(f'your score: {score}')
            print(f'ai score: {score1}')
        elif  i=='scissors'and o=='rock':
            print('ai text:',o)
            lose()
            score1=score1+1
            print(f'your score: {score}')
            print(f'ai score: {score1}')
        elif i=='rock'and o=='paper':
            print('ai text:',o)
            lose()
            score1=score1+1
            print(f'your score: {score}')
            print(f'ai score: {score1}')
        elif i=='paper'and o=='rock':
            print('ai text:',o)
            Win()
            score=score+1
            print(f'your score: {score}')
            print(f'ai score: {score1}')
        elif o=='rock'and i=='rock':
            print('ai text:',o)
            equal()
            print(f'your score: {score}')
            print(f'ai score: {score1}')
        elif i=='scissors'and o=='paper':
            print('ai text:',o)
            Win()
            score=score+1
            print(f'your score: {score}')
            print(f'ai score: {score1}')

        elif i=='paper' and o=='scissors':
            print('ai text:',o)
            lose()
            score1=score1+1
            print(f'your score: {score}')
            print(f'ai score: {score1}')
        elif i=='scissors' and o=='scissors':
            print('ai text:',o)
            equal()
            print(f'your score: {score}')
            print(f'ai score: {score1}')
        elif i=='paper' and o=='paper':
            print('ai text:',o)
            equal()
            print(f'your score: {score}')
            print(f'ai score: {score1}')
        else:
    
            try:
                print('your text is incorrect')
                l=l+1
                continue
        
            except (NameError,ValueError):
                pass
    
  
        if l==0:
            if score > score1:
                m()
            elif score1 > score:
                k()
            elif score == score1:
                cowsay.cow('your score is equal than ai')
            elif r==score:
                Win()
            elif r==score1:
                lose()
        if l==0 :
            break
if y=="2" or y=="play with friend":
    l=int(input("number of round?"))
    yi=str(l)
    copy=yi
    
    with open("round.csv","a") as file:
        file.write(yi)
    score1=int()
    score2=int()
    for w in range(l):
        
        check=input("do you want to check?")
        if check=="":
            with open("score.csv","r") as fa:
                g=fa.read()
            user1,user2=g.split(",")
            if (user1=="scissors" and user2=="scissors") or (user1=="rock" and user2=="rock") or (user1=="paper" and user2=="paper"):
                print(f"user1 text: {user1} user2 text: {user2}")
                print(f"user1 score: {score1} user2 score: {score2}")
                print("equal")
                
            if user1=="scissors" and user2=="paper" or user1=="rock" and user2=="scissors" or user1=="paper" and user2=="rock":
                print(f"user1 text: {user1} user2 text: {user2}")
                print(f"user1 score: {score1+1} user2 score: {score2}")
                print("user1 winner this round")
            if user2=="scissors" and user1=="paper" or user2=="rock" and user1=="scissors" or user2=="paper" and user1=="rock":
                print(f"user1 text: {user1} user2 text: {user2}")
                print(f"user1 score: {score1} user2 score: {score2+1}")
                
                print("user2 is winner the game")
            with open("round.csv","a") as file:
                file.write(yi)
            if w==copy:
                if score1==copy or user1>user2:
                    print("user1 is winner this game")
                if score2 == copy or user2>user1:
                    print("user2 is winner this game")
                if score1==score2:
                    print("user1 and user2 has equal")
                    
                
            
            
                

    
       