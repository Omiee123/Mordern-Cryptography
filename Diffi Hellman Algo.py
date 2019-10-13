#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Diffi Hellman Key Exchange Algorithm
#Step 1 : Choose Random Number A,B (Private Random Number)
#Step 2 : Choose g and p (Shared Value)
#Step 3 : Find Xa and Xb (Xa = g**a mod p & Xb = g**b mod p)
#Step 4 : Share Xa and Xb
#Step 5 : Key Generation k = Xb**a mod p = xa**b mod p


# In[2]:


#Step 1 : Choose Random Number A,B (Private Random Number)
A = int(input("Choose Random Number for A : "))
B = int(input("Choose Random Number for B : "))


# In[3]:


#Step 2 : Choose g and p (Shared Value)
g = int(input("Enter g : "))
p = int(input("Enter p : "))


# In[9]:


#Step 3 : Find Xa and Xb (Xa = g**a mod p & Xb = g**b mod p)
xa = (g**A)%p
xb = (g**B)%p
#calculated individually
#Step 4 : Share Xa and Xb
print("xa : "+str(xa))
print("xb : "+str(xb))


# In[7]:


#Step 5 : Key Generation k = Xb**a mod p = xa**b mod p
print("Key Recived by xa")
k_A = (xb**A)%p
print("k : "+str(k_A))

print("Key Recived by xb")
k_B = (xa**B)%p
print("k : "+str(k_B))


# In[ ]:




