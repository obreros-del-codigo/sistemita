import main

def foo_input():
    print("here")
    xf=0.1
    yf=1.0
    zf=10.0
    file_flag = False
    formulae_str = 'x'
    equation_flag=False
    n=len(sys.argv)

    for i in range(n):
        if '-f' in sys.argv[i]:
            file_flag =True
            filename=sys.argv[i+1]
        if '-e' in sys.argv[i]:
            equation_flag =True
            formulae_str=sys.argv[i+1]    

    if file_flag:
        with open('formulae.dat') as f:
            formulae=f.readlines()
            formulae_str=formulae[0]
            print("Using archive mode with "+formulae_str)
    if equation_flag:
        print("Using equation "+formulae_str)
        
    return inputs 
    
