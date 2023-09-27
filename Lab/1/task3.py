#the two numbers are multiplied by continusouly adding one of them times the other
def mul(a, b):
    sum = 0
    
    while (b>0):
        sum = sum + a
        b =  b -1
    return sum 


list1= [1,2,3,4]
list2= [1,2,3,4]
list3 = list()

list3 = list(map(mul, list1,list2))

# version 2 
list4 = list()
count = 0
element = 0


while(count< len(list1)):
    element  = mul(list1[count],list2[count])
    list4.append(element)
    count= count + 1
            
        
print(list3,list4)