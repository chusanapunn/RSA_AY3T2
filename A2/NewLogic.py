import math
import tkinter as tk


global n
global p
global q 
global r 

def input_prime(p,q):
    print("PLEASE ENTER THE 'p' AND 'q' VALUES BELOW:")
    p = int(input("Enter a prime number for p: "))
    q = int(input("Enter a prime number for q: "))
    print("*****************************************************")


def prime_check(a):
    if isinstance(a, int):
        if(a==2):
            return True
        elif((a<2) or ((a%2)==0)):
            return False
        elif(a>2):
            for i in range(2,a):
                if not(a%i):
                    return False
        return True

    

#New RSA Modulus 
def n_value(p,q):
    n = p * q
    print("RSA Modulus(n) is:",n)
    return n
   



# Eulers Toitent Function 
def r_value(p,q):
    r= (p-1)*(q-1)
    print("Eulers Toitent(r) is:", r)
    print("*****************************************************")
    return r

#Euclid's Algorithm
def eugcd(e,r):
    for i in range(1,r):
        while(e!=0):
            a,b=r//e,r%e
            if(b!=0):
                print("%d = %d*(%d) + %d"%(r,a,e,b))
            r=e
            e=b
 
#Extended Euclidean Algorithm
def eea(a,b):
    if(a%b==0):
        return(b,0,1)
    else:
        gcd,s,t = eea(b,a%b)
        s = s-((a//b) * t)
        print("%d = %d*(%d) + (%d)*(%d)"%(gcd,a,t,s,b))
        return(gcd,t,s)
 
#Multiplicative Inverse
def mult_inv(e,r):
    gcd,s,_=eea(e,r)
    if(gcd!=1):
        return None
    else:
        if(s<0):
            print("s=%d. Since %d is less than 0, s = s(modr), i.e., s=%d."%(s,s,s%r))
        elif(s>0):
            print("s=%d."%(s))
        return s%r
#GCD
'''CALCULATION OF GCD FOR 'e' CALCULATION.'''    
def egcd(e,r):
    while(r!=0):
        e,r=r,e%r
    return e

#Value Calculation 
def value_calculation(r):
    for i in range(1,1000):
        if(egcd(i,r)==1):
            e=i
        #check e calculation
        #print("The value of e is:",e)
    return e

#Encryption
'''ENCRYPTION ALGORITHM.'''
def encrypt(pub_key,n_text):
    e,n=pub_key
    x=[]
    m=0
    for i in n_text:
        i =str(i)
        if(i.isupper()):
            m = ord(i)-65
            c=(m**e)%n
            x.append(c)
        elif(i.islower()):               
            m= ord(i)-97
            c=(m**e)%n
            x.append(c)
        elif(i.isspace()):
            spc=400
            x.append(400)
    return x
     

#Decryption
'''DECRYPTION ALGORITHM'''
def decrypt(priv_key,c_text):
    d,n=priv_key
    c_text=str(c_text)
    txt=c_text.split(',')
    x=''
    m=0
    for i in txt:
        if(i=='400'):
            x+=' '
        else:
            m=(int(i)**d)%n
            m+=65
            c=chr(m)
            x+=c
    return x