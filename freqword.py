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
       data = data + line.strip("\n")
    return data
#dat=readFile("README.md") # test call
#print(dat) # test print

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
    for i in range(len(text)-patlen):
        newpat=text[i:patlen+i]
        if HammingDistance(pattern,newpat)<=d:
            count += 1
            #print("index: "+str(i)) # for printing the indexes of mismatch
    return count
    
    
a="GATTACATTTATCACACACTTAAGGCTGTGAGCAT" # len 35 test string
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

print(RevComp('GATTACA'))

# Code for FrequentWordsWithMRC
def FrequentWordsWithMRC(text,k,d):
    FreqPat={}
    count=[]
    for i in range(len(text)-k):
        pat=text[i:k+i]
        cnt1=ApproximatePatternCount(text,pat,d)
        cnt2=ApproximatePatternCount(text,RevComp(pat),d)
        count.append(cnt1+cnt2)






