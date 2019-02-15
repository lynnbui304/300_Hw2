def readFile(file_name):
    data = ""
    file = open(file_name, "r")
    for line in file:
       data = data + line 
    return data 
	
def patternCount(data, pattern):
    count = 0

    data_len = len(data)
    pattern_len = len(pattern)

    for i in range(data_len - pattern_len):
	    if (data[i:i+pattern_len] == pattern):
		    count = count + 1
    return count
	
pattern = "atgatcaag"	
data = readFile("VibrioOriC.txt")
count = patternCount(data,pattern)
print ("The pattern is: ", pattern) 
print ("The count is: ", count)