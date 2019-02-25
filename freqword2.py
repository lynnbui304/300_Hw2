# freqword2.py
# 
# Written by: Steven Parker and Lynn Bui
#
# 
#########################################

# Create uppercase string of dna
def readFile(file_name):
    data = ""
    file = open(file_name, "r")
    #next(file) # optional for first line skip
    for line in file:
       data = data + line.strip("\n").upper() # Remove \n and change to uppercase
    return data

# Hamming Distance function
def HammingDistance(pat1,pat2,d):
    count=0
    for i in range(len(pat1)): # Check for differences in patterns
        if pat1[i] != pat2[i]:
            count += 1
        if d < count:
            return False # return False if over hamming distance
    return True # return True if at or under hamming distance

# Code for approximate pattern count
def ApproximatePatternCount(text, pattern, d, index):
    count = 0
    patlen = len(pattern)
    loc=[]
    for i in range(len(text)-patlen+1): # Check each position for hamming distance d
        newpat = text[i:patlen+i]
        if HammingDistance(pattern, newpat, d):
            count += 1
            loc.append(i+index)
    return [count,loc]

# Code for reverse compliment
def RevComp(pat):
    revC=''
    for i in pat: # Swap each compliment 
        if i == 'A':
            revC += 'T'
        if i == 'T':
            revC += 'A'
        if i == 'G':
            revC += 'C'
        if i == 'C':
            revC += 'G'
    return revC[::-1] #  return reverse compliment

# Code for FrequentWordsWithMRC
def FrequentWordsWithMRC(text,k,d):
    dict={} # Dictionary
    FreqPat={} # set for final output
    count = [] # Array of score and match locations
    for i in range(len(text)-k+1):
        count.append([1,[i]])
    for i in range(len(text)-k+1):
        # print(i) # optional print current index to test for reasonable speed
        pat = text[i:k+i]
        rPat = RevComp(pat)
        if pat in dict:
            count[i]=dict[pat]
        else:
            cnt1 = ApproximatePatternCount(text[i+1:], pat, d, i+1)
            cnt2 = ApproximatePatternCount(text[i:], rPat, d, i)
            count[i][0]+=cnt1[0]+cnt2[0]
            count[i][1]+=cnt1[1]+cnt2[1]
            for j in cnt1[1]+cnt2[1]:
                if j > i:
                    count[j][0]+=1
                    count[j][1]+=[i]
            dict[pat]=count[i]
    M = max(count, key=lambda x: x[0])
    for i in dict:
        if dict[i][0] == M[0]:
            if i not in FreqPat:
                FreqPat[i]=dict[i]
    return FreqPat

dat = readFile("VibrioOriC.txt") #  read file
print(FrequentWordsWithMRC(dat,9,1))