# freqword.py
# 
# Written by: Steven Parker and Lynn Bui
#
# 
#########################################

def readFile(file_name):
    data = ""
    file = open(file_name, "r")
    for line in file:
       data = data + line.strip("\n").upper()
    return data
dat=readFile("VibrioOriC.txt") # read file
#print(dat) # test print
=======
>>>>>>> Stashed changes

# Hamming Distance function
def HammingDistance(pat1,pat2):
    count=0
    for i in range(len(pat1)):
        if pat1[i] != pat2[i]:
            count += 1
    return count

# Code for approximate pattern count
def ApproximatePatternCount(text,pattern,d):
    count = 0
    patlen = len(pattern)
    for i in range(len(text)-patlen+1):
        newpat=text[i:patlen+i]
        if HammingDistance(pattern,newpat)<=d:
            count += 1
            #print("index: "+str(i)) # for printing the indexes of mismatch
    return count
    
    
#a="GATTACATTTATCACACACTTAAGGCTGTGAGCAT" # len 35 test string
#="GATTACA" # test pattern
#app=ApproximatePatternCount(a,b,3) # test call
#print(app) # test call

# Code for reverse compliment
def RevComp(pat):
    revC=''
    for i in pat:
        if i == 'A':
            revC += 'T'
        if i == 'T':
            revC += 'A'
        if i == 'G':
            revC += 'C'
        if i == 'C':
            revC += 'G'
    return revC[::-1]

#print(RevComp('GATTACA')) # RevComp test

# Code for FrequentWordsWithMRC
def FrequentWordsWithMRC(text,k,d):
    FreqPat={}
    count=[]
    for i in range(len(text)-k+1):
        pat=text[i:k+i]
        cnt1=ApproximatePatternCount(text,pat,d)
        cnt2=ApproximatePatternCount(text,RevComp(pat),d)
        count.append(cnt1+cnt2)
    M=max(count)
    for i in range(len(count)):
        if count[i]==M:
            if text[i:k+i] in FreqPat:
                FreqPat[text[i:k+i]].append(i)
            else:
                FreqPat[text[i:k+i]]=[i]
    return M,FreqPat
print(FrequentWordsWithMRC(dat,9,0))







