# freqword.py
#
# Written by: Steven Parker and Lynn Bui
######################

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
    #print("count: "+str(count)+" patlen: "+str(patlen))
    for i in range(len(text)-patlen):
        #print("i: "+str(i)+" range: "+str(len(range(len(text)-patlen)))
        newpat=text[i:patlen+i]
        #print("newpat: "+newpat)
        if HammingDistance(pattern,newpat)<=d:
            count += 1
            print("index: "+str(i))
    return count
    
    
a="GATTACATTTATCACACACTTAAGGCTGTGAGCAT" #35
b="GATTACA"
app=ApproximatePatternCount(a,b,3)
print(app)



# Code for FrequentWordsWithMRC
def FrequentWordsWithMRC():
    pass







