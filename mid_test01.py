def INPUT():
    n=int(input())
    if(0<n<5):
        l=int(input())
        if(0<n<5 and 2<l<12 and l%2!=0):
            return n,l
        else:
            print("error")
            exit()
    else:
        print("error")    
        exit()

def number(j):
    for i in range(1,j+1):
        print(i,end="")

def numbernimus(j):
    for i in range(j,0,-1):
        print(i,end="")

def main(): 
    n,l=INPUT()
    if(n==1):
        for i in range(1,l+1,1):
            print("*"*(l-i),end="")
            print("_",end="")
            print("*"*i,end="")
            print()
    elif(n==2):
        for i in range(1,l+1,1):
            number(i)
            print("*"*(l*2-i*2),end="")
            numbernimus(i)
            print()
    elif(n==3):
        print('_'*l+'#'+'_'*l)
        for i in range(1,l//2+1):
            print('#'*i,end="")
            print('_'*(l-2*i),end="")
            print('#',end="")
            print('_'*(2*i-1),end="")
            print('#',end="")
            print('_'*(l-2*i),end="")
            print('#'*i,end="")
            print()
        
        for i in range(l//2-1,0,-1):
            print('#'*i,end="")
            print('_'*(l-2*i),end="")
            print('#',end="")
            print('_'*(2*i-1),end="")
            print('#',end="")
            print('_'*(l-2*i),end="")
            print('#'*i,end="")
            print()
        print('_'*l+'#'+'_'*l)
    elif(n==4):
        for i in range(1,l//2+1):
            print("*"*i,end="")
            print("_"*(l-2*i),end="")
            print("*"*i,end="")
            print()
        print("*"*l)
        for i in range(1,l//2+1):
            print('_'*i,end="")
            print("*"*(l-2*i),end="")
            print("_"*i,end="")
            print()
            
if(__name__=="__main__"):
    main()