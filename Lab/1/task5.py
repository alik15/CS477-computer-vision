# create file if it doesnt exist 
# read and display file contents 
# append data to file 


####################################
# reg number goes here 

reg_number = 336676
#create
try:
    open("lab2.txt","x")
except:
    print("file already exists")

#read
with open("lab2.txt","r") as file:
    print(file.read())
    
    
    
#write 
with open("lab2.txt","a") as file:
    file.write(f"My registration number is {reg_number}")
    
    
    
#read
with open("lab2.txt","r") as file:
    print(file.read())
    

    