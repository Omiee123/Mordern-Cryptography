#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Step 1 : n = P x Q
# Step 2 : fi(n) = (P-1)X(Q-1)
# Step 3 : e : e should lie between 1 to fn and gcd(e,fn) = 1
# Step 4 : {e,n}
# Step 5 : ASCII Value of M
# Step 6 : E = (M**e)%n
# Step 7 : Decryption : Multiplicative Inverse of e w.r.t to fi(n)
# Step 8 : Decryption : D = e^(-1) mod fi(n)

def gcd(a,b):
    if a==0:
        return b
    
    return gcd(b%a,a)

def multiplicative_inverse(x, y):
    a1,b1 = 1,0
    a2,b2 = 0,1
    a3,b3 = (x,y) if x > y else (y,x)
    
    large = a3
    res = 0
    #print(a1,a2,a3,b1,b2,b3)
    
    while b3 != 1:
        div = int(a3/b3)
        #print("div : {}".format(div))
        t1 = a1 - (div * b1)
        t2 = a2 - (div * b2)
        t3 = a3 - (div * b3)
        
        a1,a2,a3 = b1,b2,b3
        b1,b2,b3 = t1,t2,t3
        
    res = b2 if b2 > 0 else (large+b2)
    
    return res

# Step 1 : n = P x Q
P = int(input("Enter prime number P : "))
Q = int(input("Enter prime number Q : "))
n = P*Q
print("n : {}".format(n))

# Step 2 : fi(n) = (P-1)X(Q-1)
fn = (P-1)*(Q-1)
print("fn : {}".format(fn))

# Step 3 : e
e = int(input("Enter number e : "))
while e > fn or e < 1 or gcd(e,fn)!=1:
    print("Condition of e is not satisfied")
    e=int(input("Enter number e : "))

# Step 4 : {e,n}
print("pu_key = ({},{})".format(e,n))

# Step 5 : ASCII Value of M
M = input("Enter Message M : ")
M = M.upper()
M = M.replace(" ","")
print(M)
ascii_array = [ ord(i) for i in M ]
print(ascii_array)

# Step 6 : E = (M**e)%n
result_array = ["x"]*len(ascii_array)
print(result_array)
for i in range(0,len(ascii_array)):
    result_array[i] = (ascii_array[i]**e)%n
    
print(result_array)

# Step 7 : Decryption : Multiplicative Inverse of e w.r.t to fi(n)
e1 = multiplicative_inverse(13, 352)
print("Private Key : ({},{})".format(e1,n))

# Step 8 : Decryption : D = c1**e^(-1) mod fi(n)
output_array = ["x"]*len(ascii_array)
print(output_array)
for i in range(0,len(ascii_array)):
    output_array[i] = (result_array[i]**e1)%n
    
print(output_array)

# Step 9 : Resultant String
result = ""

for i in range(0,len(ascii_array)):
    result += chr(output_array[i])
    
print(result)
