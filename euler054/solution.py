#!/usr/bin/python
#Poker hands
from string import maketrans 



def isAWinning(str):
    str=str.split();
    strA=sortCards(str[0:5])
    strB=sortCards(str[5:10])
    print strA,strB
    if isRoyalFlush(strA)!=isRoyalFlush(strB): return isRoyalFlush(strA)>isRoyalFlush(strB)
    if isStraightFlush(strA)!=isStraightFlush(strB): return isStraightFlush(strA)>isStraightFlush(strB)
    if isFourKind(strA)!=isFourKind(strB): return isFourKind(strA)>isFourKind(strB)
    if isFullHouse(strA,1)!=isFullHouse(strB,1): return isFullHouse(strA,1)>isFullHouse(strB,1)
    if isFullHouse(strA,2)!=isFullHouse(strB,2): return isFullHouse(strA,2)>isFullHouse(strB,2)


    if isFlush(strA)!=isFlush(strB): return isFlush(strA)>isFlush(strB)

    if isStraight(strA)!=isStraight(strB): return isStraight(strA)>isStraight(strB)

    if isThreeKind(strA)!=isThreeKind(strB): return isThreeKind(strA)>isThreeKind(strB)


    if isTwoPair(strA,1)!=isTwoPair(strB,1): return isTwoPair(strA,1)>isTwoPair(strB,1)
    if isTwoPair(strA,2)!=isTwoPair(strB,2): return isTwoPair(strA,2)>isTwoPair(strB,2)
    if isPair(strA)!=isPair(strB): return isPair(strA)>isPair(strB)


    return isAHigh(strA, strB);


def sortCards(cards):
    inTable="23456789TJQKA"
    outTable="abcdefghijklm"
    tranTable = maketrans(inTable, outTable)
    l=len(cards)
    for i in range(0,l):
        cards[i]=cards[i].translate(tranTable)
    cards.sort(key=lambda cards:cards[0])
    # print cards
    return cards


def isAHigh(fiveCardsA, fiveCardsB):
    str0A=[x[0] for x in reversed(fiveCardsA)]
    str0B=[x[0] for x in reversed(fiveCardsB)]
    result=cmp(str0A, str0B)
    if result==1:
        return True
    else:
        return False

def isPair(fiveCards):
    print fiveCards
    if fiveCards[0][0]==fiveCards[1][0]:return ord(fiveCards[0][0])
    if fiveCards[1][0]==fiveCards[2][0]:return ord(fiveCards[1][0])
    if fiveCards[2][0]==fiveCards[3][0]:return ord(fiveCards[2][0])
    if fiveCards[3][0]==fiveCards[4][0]:return ord(fiveCards[3][0])
    return -1;

def isTwoPair(fiveCards,set):
    if fiveCards[0][0]==fiveCards[1][0] and fiveCards[2][0]==fiveCards[3][0]:
        if set==1: return ord(fiveCards[2][0])
        else: return ord(fiveCards[0][0])
    if fiveCards[0][0]==fiveCards[1][0] and fiveCards[3][0]==fiveCards[4][0]:
        if set==1: return ord(fiveCards[3][0])
        else: return ord(fiveCards[0][0])
    if fiveCards[1][0]==fiveCards[2][0] and fiveCards[3][0]==fiveCards[4][0]:
        if set==1: return ord(fiveCards[3][0])
        else: return ord(fiveCards[1][0])
    return -1;

def isThreeKind(fiveCards):
    if fiveCards[0][0]==fiveCards[1][0]==fiveCards[2][0]: return ord(fiveCards[0][0])
    if fiveCards[1][0]==fiveCards[2][0]==fiveCards[3][0]: return ord(fiveCards[1][0])
    if fiveCards[2][0]==fiveCards[3][0]==fiveCards[4][0]: return ord(fiveCards[2][0])
    return -1;                

def isStraight(fiveCards):
    if ord(fiveCards[4][0])-ord(fiveCards[3][0])==ord(fiveCards[3][0])-ord(fiveCards[2][0])==ord(fiveCards[2][0])-ord(fiveCards[1][0])==ord(fiveCards[1][0])-ord(fiveCards[0][0])==1:
        # print fiveCards, ' isStraight'
        return ord(fiveCards[4][0])
    return -1;

def isFlush(fiveCards):
    if fiveCards[0][1]==fiveCards[1][1]==fiveCards[2][1]==fiveCards[3][1]==fiveCards[4][1]:
        # print fiveCards, ' isFlush'
        return ord(fiveCards[4][1])
    return -1;

def isFullHouse(fiveCards,set):#set: 1 or 2
    if fiveCards[0][0]==fiveCards[1][0]==fiveCards[2][0] and fiveCards[3][0]==fiveCards[4][0]:
        if set==1: return ord(fiveCards[0][0])
        else:   return ord(fiveCards[3][0])
    if fiveCards[0][0]==fiveCards[1][0] and fiveCards[2][0]==fiveCards[3][0]==fiveCards[4][0]:
        if set==1: return ord(fiveCards[2][0])
        else:   return ord(fiveCards[0][0])
    return -1

def isFourKind(fiveCards):
    if fiveCards[0][0]==fiveCards[1][0]==fiveCards[2][0]==fiveCards[3][0]:
        return ord(fiveCards[0][0])
    if fiveCards[1][0]==fiveCards[2][0]==fiveCards[3][0]==fiveCards[4][0]:
        return ord(fiveCards[1][0])
    return -1

def isStraightFlush(fiveCards):
    if isFlush(fiveCards)>0 and isStraight(fiveCards)>0:
        return ord(fiveCards[4][0])
    return -1

def isRoyalFlush(fiveCards):
    if isFlush(fiveCards)==109:
        return 109
    return -1

def main():
    myfile=open("poker.txt","r")
    lines = myfile.read().splitlines()
    # lines=lines[0:10]
    count=0
    for line in lines:
        if isAWinning(line):
            # print '>'
            count+=1
        # else:
        #     print '<'
    
    print count

main()

# assert(isAWinning('5H 5C 6S 7S KD 2C 3S 8S 8D TD')==False)
# assert(isAWinning('5D 8C 9S JS AC 2C 5C 7D 8S QH')==True)
# assert(isAWinning('2D 9C AS AH AC 3D 6D 7D TD QD')==False)
# assert(isAWinning('4D 6S 9H QH QC 3D 6D 7H QD QS')==True)
# assert(isAWinning('2H 2D 4C 4D 4S 3C 3D 3S 9S 9D')==True)


# sortCards(['JD','TC','AS','QD','KD'])