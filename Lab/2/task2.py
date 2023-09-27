#prompt for size of list 

size_of_list= int(input("Please Enter the size of the list you want: "))
user_items = list()

while(size_of_list>0):
    element_entered = input("Enter the element you want to enter in the list: ")
    user_items.append(element_entered)
    size_of_list = size_of_list - 1
    
print(user_items)