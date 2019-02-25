# freqword.py 
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
# print(dat) # test print 
 
# Hamming Distance function 
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
def ApproximatePatternCount(text, pattern, d): 
    count = 0 
    patlen = len(pattern) 
    for i in range(len(text)-patlen+1): # Check each position for hamming distance d 
        newpat = text[i:patlen+i] 
        if HammingDistance(pattern, newpat, d): 
            count += 1 
    return count 
 
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
    count = [] # Array of score for each pattern starting at each index 
    for i in range(len(text)-k+1): 
        # print(i) 
        pat = text[i:k+i] 
        rPat = RevComp(pat) 
        if pat in dict: 
            count.append(dict[pat]) 
        elif rPat in dict: 
            count.append(dict[rPat]) 
        else: 
            cnt1 = ApproximatePatternCount(text, pat, d) 
            cnt2 = ApproximatePatternCount(text, rPat, d) 
            count.append(cnt1+cnt2) 
            dict[pat]=cnt1+cnt2 
    M = max(count) 
    for i in range(len(count)): 
        if count[i] == M: 
            if text[i:k+i] in FreqPat: 
                FreqPat[text[i:k+i]].append(i) 
            else: 
                FreqPat[text[i:k+i]]=[i] 
    return [M,FreqPat] 

dat = readFile("VibrioOriC.txt") #  read file 
print(FrequentWordsWithMRC(dat,9,0)) 