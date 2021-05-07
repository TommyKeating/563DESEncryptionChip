IN = [1,1,1,0,1,1,0,0]
KEY = [1,1,0,0,0,1,0,1,1,0]

#Hard coded shifting of bits
def LCS(bits, places):
    if(places == 1):
        return [bits[1],bits[2],bits[3],bits[4],bits[0],bits[6],bits[7],bits[8],bits[9],bits[5]]
    if(places == 3):
        return [bits[3],bits[4],bits[0],bits[1],bits[2],bits[8],bits[9],bits[5],bits[6],bits[7]]

def XOR(a,b,size):
    result = []
    for x in range(size):
        if(a[x] == b[x]):
            result.append(0)
        else:
            result.append(1)
    return result

def SBOX1(red):
    result = []
    if(red[1] == 0 and red[2] == 0):
        if(red[0] == 0 and red[3] == 0):
            result = [0,1]
        elif(red[0] == 0 and red[3] == 1):
            result = [1,1]
        elif(red[0] == 1 and red[3] == 0):
            result = [0,0]
        else:
            result = [1,1]
    elif(red[1] == 0 and red[2] == 1):
        if(red[0] == 0 and red[3] == 0):
            result = [0,0]
        elif(red[0] == 0 and red[3] == 1):
            result = [1,0]
        elif(red[0] == 1 and red[3] == 0):
            result = [1,0]
        else:
            result = [0,1]
    elif(red[1] == 1 and red[2] == 0):
        if(red[0] == 0 and red[3] == 0):
            result = [1,1]
        elif(red[0] == 0 and red[3] == 1):
            result = [0,1]
        elif(red[0] == 1 and red[3] == 0):
            result = [0,1]
        else:
            result = [1,1]
    else:
        if(red[0] == 0 and red[3] == 0):
            result = [1,0]
        elif(red[0] == 0 and red[3] == 1):
            result = [0,0]
        elif(red[0] == 1 and red[3] == 0):
            result = [1,1]
        else:
            result = [1,0]
    return result

def SBOX2(red):
    result = []
    if(red[1] == 0 and red[2] == 0):
        if(red[0] == 0 and red[3] == 0):
            result = [0,0]
        elif(red[0] == 0 and red[3] == 1):
            result = [1,0]
        elif(red[0] == 1 and red[3] == 0):
            result = [1,1]
        else:
            result = [1,0]
    elif(red[1] == 0 and red[2] == 1):
        if(red[0] == 0 and red[3] == 0):
            result = [0,1]
        elif(red[0] == 0 and red[3] == 1):
            result = [0,0]
        elif(red[0] == 1 and red[3] == 0):
            result = [0,0]
        else:
            result = [0,1]
    elif(red[1] == 1 and red[2] == 0):
        if(red[0] == 0 and red[3] == 0):
            result = [1,0]
        elif(red[0] == 0 and red[3] == 1):
            result = [0,1]
        elif(red[0] == 1 and red[3] == 0):
            result = [0,1]
        else:
            result = [0,0]
    else:
        if(red[0] == 0 and red[3] == 0):
            result = [1,1]
        elif(red[0] == 0 and red[3] == 1):
            result = [1,1]
        elif(red[0] == 1 and red[3] == 0):
            result = [0,0]
        else:
            result = [1,1]
    return result

#Create P10
P10 = [KEY[2],KEY[4],KEY[1],KEY[6],KEY[3],KEY[9],KEY[0],KEY[8],KEY[7],KEY[5]]
#Do the shift to find Key 1
Shift1 = LCS(P10, 1)
Key1 = [Shift1[5],Shift1[2],Shift1[6],Shift1[3],Shift1[7],Shift1[4],Shift1[9],Shift1[8]]
#Do the shift to find Key 2
Shift2 = LCS(P10, 3)
Key2 = [Shift2[5],Shift2[2],Shift2[6],Shift2[3],Shift2[7],Shift2[4],Shift2[9],Shift2[8]]


#Find IP
IP = [IN[1],IN[5],IN[2],IN[0],IN[3],IN[7],IN[4],IN[6]]

#Work for F1
#Generate E/P(R)
EPR1 = [IP[7],IP[4],IP[5],IP[6],IP[5],IP[6],IP[7],IP[4]]
#Exclusive OR Key 1 and E/P(R)
KEP1=XOR(Key1,EPR1,8)
#Go through first Sbox
red1 = SBOX1([KEP1[0],KEP1[1],KEP1[2],KEP1[3]])
#Go through second Sbox
green1 = SBOX2([KEP1[4],KEP1[5],KEP1[6],KEP1[7]])
#COmbine results
boxed1 = [red1[0],red1[1],green1[0],green1[1]]
#Use P4
P41 = [boxed1[1],boxed1[3],boxed1[2],boxed1[0]]
#XOR L and F
F1 = XOR(P41,[IP[0],IP[1],IP[2],IP[3]],4)
#Combine for answer
FK1 = [F1[0],F1[1],F1[2],F1[3],IP[4],IP[5],IP[6],IP[7]]
print(FK1)
#Do SW swap L and R
SW = [FK1[4],FK1[5],FK1[6],FK1[7],FK1[0],FK1[1],FK1[2],FK1[3]]

#Work for F2
#Generate E/P(R)
EPR2 = [SW[7],SW[4],SW[5],SW[6],SW[5],SW[6],SW[7],SW[4]]
#Exclusive OR Key 1 and E/P(R)
KEP2=XOR(Key2,EPR2,8)
#Go through first Sbox
red2 = SBOX1([KEP2[0],KEP2[1],KEP2[2],KEP2[3]])
#Go through second Sbox
green2 = SBOX2([KEP2[4],KEP2[5],KEP2[6],KEP2[7]])
#COmbine results
boxed2 = [red2[0],red2[1],green2[0],green2[1]]
#Use P4
P42 = [boxed2[1],boxed2[3],boxed2[2],boxed2[0]]
#XOR L and F
F2 = XOR(P42,[SW[0],SW[1],SW[2],SW[3]],4)
#Combine for answer
FK2 = [F2[0],F2[1],F2[2],F2[3],SW[4],SW[5],SW[6],SW[7]]

#Using -IP defined in handout finish
ENCRYPT = [FK2[3],FK2[0],FK2[2],FK2[4],FK2[6],FK2[1],FK2[7],FK2[5]]
print(ENCRYPT)
