

# Example usage:
my_list = [64, 25, 12, 22, 11]


my_list1 =[5,8,2,3,11,6]

def selection_sort(input_list):
    for index_of_i,i in enumerate(input_list):
        min_index = index_of_i

        for index_of_j, j in enumerate(input_list):
            if j < i:
                min_index = index_of_j
             
             
                temp = input_list[min_index]
                input_list[min_index] = input_list[i]
                input_list[i] = temp
                
        print(my_list1)
            
          
        
selection_sort(my_list1)
        
                    
        
print(my_list1)
