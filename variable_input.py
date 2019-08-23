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
    inputs=[]
    for i in range(n):
        if '-f' in sys.argv[i]:
            file_flag =True
            filename=sys.argv[i+1]
        if '-e' in sys.argv[i]:
            equation_flag =True
            formulae_str=sys.argv[i+1]
            inputs.append(formulae_str)
#        else:
#            raise TypeError "no hay ecuacion"
        if '-a' in sys.argv[i]:
            equation_flag =True
            a=sys.argv[i+1]
            inputs.append(a)
        else:
            inputs.append(1)
        if '-b' in sys.argv[i]:
            equation_flag =True
            b=sys.argv[i+1]
            inputs.append(b)
        else:
            inputs.append(1)
            
        if '-x0' in sys.argv[i]:
            equation_flag =True
            x0=sys.argv[i+1]
            inputs.append(x0)
        else:
            inputs.append(0.1)
        if '-i' in sys.argv[i]:
            equation_flag =True
            it=sys.argv[i+1]
            inputs.append(it)
        else:
            inputs.append(10)
        if '-n' in sys.argv[i]:
            equation_flag =True
            n=sys.argv[i+1]
            inputs.append(n)
        else:
            inputs.append(2)
            
            

    if file_flag:
        with open('formulae.dat') as f:
            formulae=f.readlines()
            formulae_str=formulae[0]
            print("Using archive mode with "+formulae_str)
    if equation_flag:
        print("Using equation ",formulae_str,"with a:",a,",b:",b,"n:",n,", initial conditions:",x0,", iterations:",it)
    #a,b,x0,i,n
    return inputs 
    
