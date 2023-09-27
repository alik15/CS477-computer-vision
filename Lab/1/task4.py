
count = 0
list_of_keys = list()
list_of_values = list()
#version 1 


while(count<5):
    print("Please enter keys")
    print("Currently entered strings: ", count)
    key = 0
    key = str(input())
    list_of_keys.append(key)
    count= count + 1    
    
count = 0
while(count<5):
    print("Please enter the values for the previous keys you entered")
    val = 0
    val = str(input())
    list_of_values.append(val)
    count = count + 1 
    

print(dict(zip(list_of_keys,list_of_values)))


# task4 version 2

#input keys 
#input values 
