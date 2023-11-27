import math
def bigOn(n) : 
    for i in range(0,n):
        print(i)
        

def bigOn2(n) : 
    for i in range(0,n):
        for j in range(0,n):
            print(i,j)
            

def bigOn3(n): 
    for i in range(0,n):
        for j in range(0,n):
            for k in range(0,n):
                print(i,j,k)
                
            

def logn(n):
        while (n > 1 ):
            n = math.floor(n/2):
            print(n)

def nlogn(n):
    lim = n
    while n > 1 :
        n = math.floor(n/2)
        for i in range(0,lim) :
            print(i)