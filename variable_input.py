import sys
import numpy as np

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

    
    Z=10

    for i,v in enumerate(sys.argv):
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
                
    A=[a0,a1,da]
    B=[b0,b1,db]
    N=[n0,n1,dn]
    X0=[x0,x1,dx]
    A=[float(i) for i in A]
    B=[float(i) for i in B]
    N=[float(i) for i in N]
    X0=[float(i) for i in X0]
    A=np.arange(A[0],A[1]+1,A[2])
    B=np.arange(B[0],B[1]+1,B[2])
    N=np.arange(N[0],N[1]+1,N[2])
    X0=np.arange(X0[0],A[1]+1,X0[2])
    print(A)
    print(B)
    print(N)
    print(X0)
    return formulae_str,A,B,N,X0,it
    
