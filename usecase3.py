#Declaring a list
list_write=['Avoid', 'trailing', 'whitespace', 'anywhere']

#creating and opening a file
File_Obj=open("Read_txt.txt","w")

#writing it to the above file
for word in list_write:
    File_Obj.write(word+"\n")

#close the file
File_Obj.close()


