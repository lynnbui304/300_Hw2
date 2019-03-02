Written by Lynn Bui and Steven Parker
Input:
dat = DNA pattern
k = k-mer length searched for
d = max hamming distance
print(FrequentWordsWithMRC(dat,k,d))

Output:
{'pattern_1': [score, array_1], 'pattern_2': [score, array_2], ..., 'pattern_N': [score, array_N] }

Where:
 score = largest score for any k-mer with a hamming distance up to d
 array = array of locations for each match.

VibrioOriC.txt:
{'ATGATCAAG': [6, [27, 127, 508, 397, 468, 525]], 'CTTGATCAT': [6, [397, 27, 397, 468, 525, 508]]}

EColi_small.fq:
{'GCTGGCGGA': [20, [2420, 593, 1801, 3321, 4389, 4503, 4929, 5396, 5721, 6098, 6626, 7078, 7832, 8989, 9118, 9484, 11756, 3202, 3281, 6382]]}