def palindrome(input_list):
    p1 = 0
    p2 = len(input_list)
    
    count = round(len(input_list)/2)
    
    palindrome = "False"
    
    while (count > 0 ):
        p1 = p1 + 1
        p2 = p2 - 1
        if (input_list[p1]==input_list[p2-1]):
            palindrome = "is a palindrome"
        #if(input_list[p1] is input_list[p2-1]): 
        else:
            palindrome = "is not a palindrome"
        
        count = count - 1 
    return palindrome
    

#tests
list_of_tests = ['radar','level','5445','8395938', 'racecar'] 

for test in list_of_tests:
 print(f"test {palindrome(test)}")

    
