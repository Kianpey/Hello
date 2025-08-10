with open("round.csv","r") as file:
    y=file.read()
with open("round.csv","w") as rr:
    rr.write("")
y=int(y)
for v in range(y):
    n=input("scissors or paper or rock:")
    with open("score.csv","a") as f:
        f.write(f"{n}")