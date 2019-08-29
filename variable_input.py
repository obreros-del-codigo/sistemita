import sys

def foo_input():
    file_flag = False
    formulae_str = 'x'
    equation_flag=False
    variable_flag=False
    cycles=len(sys.argv)
    x0=a0=b0=n0=1.0
    x1=a1=b1=n1=1.0
    dx=da=db=dn=1.0
    
    it=10
    
    cycles=len(sys.argv)
    
    Z=10
    
    
    for i,v in enumerate(cycles):
        if '-f'==v:
            file_flag =True
            filename=sys.argv[i+1]
            
        if '-e'==v:
            equation_flag =True
            formulae_str=sys.argv[i+1]
            
        if '-n' ==v:
            n0=sys.argv[i+1]
            n1=sys.argv[i+2]
            dn=sys.argv[i+3]
            
        if '-a' ==v:
            a0=sys.argv[i+1]
            a1=sys.argv[i+2]
            da=sys.argv[i+3]
        if '-b' ==v:
            b0=sys.argv[i+1]
            b1=sys.argv[i+2]
            db=sys.argv[i+3]
            
        if '-x0'==v:
            x0=sys.argv[i+1]
            x1=sys.argv[i+2]
            dx=sys.argv[i+3]

        if '-i' ==v:
            it=sys.argv[i+1]




    if file_flag:
        with open('formulae.dat') as f:
            formulae=f.readlines()
            formulae_str=formulae[0]
            print("Using archive mode with "+formulae_str)
    if equation_flag:
        print("Using equation:",formulae_str)
        print("Using equation ",formulae_str,"with a:",a,",b:",b,"n:",n,", initial conditions:",x0,", iterations:",it)
        
    A=[a0,a1,da]
    B=[b0,b1,db]
    N=[n0,n1,dn]
    X0=[x0,x01,dx0]


    return formulae_str,A,B,N,X0
    
