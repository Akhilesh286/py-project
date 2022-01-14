src=open("text.txt","r") 
fline="newlkdkdkdmy added FIRST LINE\n"    #Prepending string 
oline=src.readlines() 
#Here, we prepend the string we want to on first line 
oline.insert(0,fline) 
src.close() 
 
 
#We again open the file in WRITE mode  
src=open("text.txt","w") 
src.writelines(oline) 
src.close() 