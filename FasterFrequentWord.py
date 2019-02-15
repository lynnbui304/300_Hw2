# This function reads text data from a text file
def readFile(file_name):
    data = ""
    file = open(file_name, "r")
    for line in file:
       data = data + line.strip("\n") 
    return data 

# This fucntion prints the frequency dictionary	
def printFreqsDict(freqs_dict):
    for key, val in freqs_dict.items():
	    print (key, "-->" , val)
	
def ComputingFrequencies(data, k):
    
    data_dict = {}

    data_len = len(data)
	
    for i in range(data_len - k):
        kmer_data = data[i:i+k]
        if kmer_data in data_dict:
            data_dict[kmer_data] = data_dict[kmer_data] + 1
        else:
            data_dict[kmer_data] = 1            		
		
    return data_dict

	
pattern = "atgatcaag"
k = 9	
genome_data = readFile("VibrioOriC.txt")
frequencies_dict = ComputingFrequencies(genome_data, k)
printFreqsDict(frequencies_dict)

print("Freq for '" + pattern + "' is", frequencies_dict[pattern]) 
