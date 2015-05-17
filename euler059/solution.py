#!/usr/bin/python
#XOR decryption



#encrypt and decrypt are the same function
#message, key are both list of int
def encrypt(message, key):
    l=len(message)
    result= [message[i]^key[i%len(key)] for i in range(l)]
    return result;


def analysis(message, keyLen):
    l=len(message)
    maxsize=0
    for i in range(l):
        if message[i]>maxsize:
            maxsize=message[i]

    # print maxsize  #94
    tempMessages=[[0 for x in range(maxsize+1)] for y in range(keyLen)] 
    key=[0 for x in range(keyLen)]
    # print tempMessages
    # print key

    for x in range(l):
        y=x%keyLen
        tempMessages[y][message[x]]+=1
        if tempMessages[y][message[x]]>tempMessages[y][key[y]]:
            key[y]=message[x]

    print tempMessages
    # print key
    a=32 #space character
    for i in range(keyLen):
        key[i]=key[i]^a

 
    return key


def main():
    with open ("cipher.txt", "r") as myfile:
        data=myfile.read()
        # data=myfile.read().replace('\n', '')
    
    data=[int(x) for x in data.split(',')]

    key=analysis(data,3)
    # print key

    # decriptedM=encrypt(data,key)

    # print sum(decriptedM)





main()

assert(encrypt([65],[42])==[107])

