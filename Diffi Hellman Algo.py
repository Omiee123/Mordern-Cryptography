#!/usr/bin/env python
# coding: utf-8

#Diffi Hellman Key Exchange Algorithm
#Step 1 : Choose Random Number A,B (Private Random Number)
#Step 2 : Choose g and p (Shared Value)
#Step 3 : Find Xa and Xb (Xa = g**a mod p & Xb = g**b mod p)
#Step 4 : Share Xa and Xb
#Step 5 : Key Generation k = Xb**a mod p = xa**b mod p

#Step 1 : Choose Random Number A,B (Private Random Number)
A = int(input("Choose Random Number for A : "))
B = int(input("Choose Random Number for B : "))

#Step 2 : Choose g and p (Shared Value)
g = int(input("Enter g : "))
p = int(input("Enter p : "))

#Step 3 : Find Xa and Xb (Xa = g**a mod p & Xb = g**b mod p)
xa = (g**A)%p
xb = (g**B)%p
#calculated individually

#Step 4 : Share Xa and Xb
print("xa : "+str(xa))
print("xb : "+str(xb))

#Step 5 : Key Generation k = Xb**a mod p = xa**b mod p
print("Key Recived by xa")
k_A = (xb**A)%p
print("k : "+str(k_A))

print("Key Recived by xb")
k_B = (xa**B)%p
print("k : "+str(k_B))
