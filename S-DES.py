#!/usr/bin/env python
# coding: utf-8

# In[1]:


#key Generation
def key_generation(key):
    
    P10 = [3,5,2,7,4,10,1,9,8,6]
    P8 = [6,3,7,4,8,5,10,9]
    
    key10 = [0]*10
    k1 = [0]*8
    k2 = [0]*8
    #Transformation Function P10
    for i in range(10):
        key10[i] = key[P10[i]-1]
        
    print("Step 1: P10 "+str(key10))
    
    #Left-shift-function
    def left_shift(key_array,sn):
        return key_array[sn:]+key_array[:sn]
        
    key10[:5] = left_shift(key10[:5],1)
    key10[5:] = left_shift(key10[5:],1)
    
    print("Step 2: LS-1"+str(key10))
    
    #Transformation Function P8
    for i in range(8):
        k1[i] = key10[P8[i]-1]
    
    #Left_Shift-function 2
    key10[:5] = left_shift(key10[:5],2)
    key10[5:] = left_shift(key10[5:],2)
    print("Step 3: LS-2"+str(key10))
    
    for i in range(8):
        k2[i] = key10[P8[i]-1]
        
    print("K1 :"+str(k1))
    print("K2 :"+str(k2))    
        
    return (k1,k2)


# In[22]:


#Encryption
def encryption(bitstring,key1,key2):
    
    IP = [2,6,3,1,4,8,5,7]
    EP = [4,1,2,3,2,3,4,1]
    s0 = [[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
    s1 = [[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]
    P4 = [2,4,3,1]
    IPi = [4,1,3,5,7,2,8,6]
    
    #decimal to binary
    def dec_binaray(num):
        result = ""

        rem_1 = 0 if num < 1 else num //2
        rem_2 = num%2
        result = str(rem_1)+str(rem_2)
        return result
    
    #function of rounds
    def encry(array,key):
        bitEP = [0]*8

        for i in range(8):
            bitEP[i] = array[EP[i]-1+4]
        #testprint
        print("Step 2.1 Expansion Function "+str(bitEP))
        
        #XOR with key
        temp_k = key
        for i in range(8):
            temp_k[i] = 1 if int(bitEP[i]) != int(temp_k[i]) else 0
        print("Step 2.2 XOR Result "+str(temp_k))
            
        #S-BOX
        part1 = s0[temp_k[0]*2+temp_k[3]][temp_k[1]*2+temp_k[2]]
        part1 = dec_binaray(part1)
        part2 = s1[temp_k[4]*2+temp_k[7]][temp_k[5]*2+temp_k[6]]
        part2 = dec_binaray(part2)

        S_result = [0]*4
        S_result[0],S_result[1],S_result[2],S_result[3] = part1[0],part1[1],part2[0],part2[1]
        print("Step 2.3 S-Box result "+str(S_result))
        
        #S - Box Transformation
        S_T4 = [0]*4
        for i in range(4):
            S_T4[i] = S_result[P4[i]-1]
            
        #testprint
        print("Step 2.4 P4 Function "+str(S_T4))
        
        #XOR with Left-Half
        for i in range(4):
            PlainIP[i] = '1' if int(PlainIP[i]) != int(S_T4[i]) else '0'
        print("Step 2.4 XOR with result of S-Box "+str(PlainIP))
        
        return PlainIP
            
    #initial Permutaion
    PlainIP = [0]*8
    for i in range(8):
        PlainIP[i] = bitstring[IP[i]-1]
    print("Step 1 Initial Permutation "+str(PlainIP))
    
    #round_1
    PlainIP = encry(PlainIP,key1)
    print("Step 2 Round Key 1"+str(PlainIP))
    
    #swap function
    PlainIP = PlainIP[4:]+PlainIP[:4]
    print("Step 3 Swap Function"+str(PlainIP))
    
    #round_2
    PlainIP = encry(PlainIP,key2)
    print("Step4 Round Key 2"+str(PlainIP))
    
    #final Permutation
    FinalIPi = [0]*8
    for i in range(8):
        FinalIPi[i] = PlainIP[IPi[i]-1]
        
    print("Step5 Inverse IP"+str(FinalIPi))      
    return FinalIPi


# In[23]:


key = input()
key1,key2 = key_generation(key)
bitstring = input()
result = encryption(bitstring,key1,key2)
print(result)

