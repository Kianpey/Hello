import random
choiced=random.randint(1,100)

while True:
    number=int(input("number:"))
    
    if number==choiced:
        print("your choiced number is correct number")
        break
    
    elif number>choiced:
        print("your number is bigger than choiced number")
        continue
    
    elif number<choiced:
        print("the choiced number is bigger than your number")
        continue
    