import sys

def foo_input():
    print("here")
    file_flag = False
    formulae_str = 'x'
    equation_flag=False
    variable_flag=False
    cycles=len(sys.argv)
    inputs=[]
    for i in range(cycles):
        if '-f' in sys.argv[i]:
            file_flag =True
            filename=sys.argv[i+1]
            break
        if '-e' in sys.argv[i]:
            equation_flag =True
            formulae_str=sys.argv[i+1]
            inputs.append(formulae_str)
            break
#        else:
#            raise TypeError "no hay ecuacion"
        if '-n' in sys.argv[i]:
            variable_flag =True
            n=sys.argv[i+1]
            inputs.append(n)
            try:
                for i in range(int(n)-1):
                   formulae_str+="*x"
            except:
                formulae_str=1
        else:
            inputs.append(2)
            formulae_str = "x*x"

        if '-a' in sys.argv[i]:
            variable_flag =True
            a=sys.argv[i+1]
            inputs.append(a)
            formulae_str=a+"*"+formulae_str
        else:
            inputs.append(1)

        if '-b' in sys.argv[i]:
            variable_flag =True
            b=sys.argv[i+1]
            inputs.append(b)
            formulae_str = formulae_str+"+"+b
        else:
            inputs.append(1)
            
        if '-x0' in sys.argv[i]:
            variable_flag =True
            x0=sys.argv[i+1]
            inputs.append(x0)
        else:
            inputs.append(0.1)
        if '-i' in sys.argv[i]:
            variable_flag =True
            it=sys.argv[i+1]
            inputs.append(it)
        else:
            inputs.append(10)


    if file_flag:
        with open('formulae.dat') as f:
            formulae=f.readlines()
            formulae_str=formulae[0]
            print("Using archive mode with "+formulae_str)
    if equation_flag:
        inputs.pop()
        print("Using equation:",formulae_str)
    #a,b,x0,i,n
    if variable_flag:
        inputs=inputs[:5]
        print("Using equation ",formulae_str,"with a:",a,",b:",b,"n:",n,", initial conditions:",x0,", iterations:",it)
    return inputs,formulae_str
    
