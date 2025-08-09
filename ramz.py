def main():
    n=input('1.create key or 2.unlock key: ')
    if n== '1' or n.strip()=='create key':
        ramz_generator()
    if n== '2' or n.strip()=='unlock key':
        ramz_unlocker()
def ramz_generator():
    b = input('What is your text? ')
    
    u = ''
    zx = 0
    r = len(b)
    
    while zx < r:
        u += f'{ord(b[zx])} '
        zx += 1

    print(u.strip())
    
    
def ramz_unlocker():
    try:
        n=input('your ramz:')
        x:list=n.split(' ')
        f=''
        for g in x:
            g=int(g)
            f+=chr(g)
        
        print(f)
        
    except ValueError:
        print('your ramz is incorect')
        
            
            
        
if __name__=='__main__':
    main()
        
    
    
    