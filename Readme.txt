Written by Lynn Bui and Steven Parker
Input:
dat = DNA pattern
k = k-mer length searched for
d = max hamming distance
print(FrequentWordsWithMRC(dat,k,d))

Output:
(M, {'pattern_1': [array_1], 'pattern_2': [array_2], ..., 'pattern_N': [array_N] })

M = Largest score for any k-mer with a hamming distance up to d

{'pattern': [array]} = a 'pattern' with a score of M and an [array] of each 
position it was found in dat