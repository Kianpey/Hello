n=input("what is your name?").title()
if "," in n:
    last,first=n.split(",")
    print(f"hello, {first} {last}")
if "," not in n:
        print(f"hello, {n}")