n=input("what is your name?").title()
if "," in n:
    last,first=n.split(",")
    print(f"hello, {first.strip()} {last.strip()}")
if "," not in n:
        print(f"hello, {n}")