with open("round.csv","r") as file:
    y=file.read()
    print(y)
y=int(y)
for v in range(y):
    n=input("scissors or paper or rock:")
    with open("score.csv","a") as f:
        f.write(f'{n},')
    
