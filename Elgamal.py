#!/usr/bin/env python
# coding: utf-8

# In[47]:


print("Welcome Alice :")
print("To Contact with Bob Generate Key")
p = int(input("Enter prime number p : "))
g = int(input("Enter g : "))
x = int(input("Choose Private Key x : "))

Y = ((g**x)%p)
#public key is Ya, g, p

#Step 1 - Sender Encrypt Plain Text With Receipient Public Key
print("Hi Bob The Public Key for Alice is {},{},{}".format(Y,g,x))
k = int(input("Enter k : "))
a = ((g**k)%p)
print("k : "+str(k))
print("a : "+str(a))

M = int(input("Enter Message : "))
b = (M*(Y**k))%p
print("b : "+str(b))


# In[48]:


#Step 2 - Receiver Decrypt Cipher Text With It's Own Private Key
Plain = ((a**(p-x-1))*b)%p
print("Original Message : "+str(Plain))


# In[ ]:


#Chek following example
#(P=71, G=33, x=62, M=15, k=31)
#(P=23, G=11, x=6, M=10, k=3)
#(P=11, G=2, x=8, M=5, k=9)
#(P=1697, G=138, x=164, M=19, k=159)

