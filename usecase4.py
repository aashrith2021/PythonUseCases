#opening the file with read access
file1 = open("Read_txt.txt","r")

#printing the words from file
print(' '.join(file1.read().split('\n')))

#closing the file
file1.close()