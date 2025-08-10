r=input("what is your name?").title()
if "," in r:
    lastname,firstname=r.split(",")
    print(f"hello, {firstname.strip()} {lastname.strip()}")
    
else:
    print(f"Hello, {r}")