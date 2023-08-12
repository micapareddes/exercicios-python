def verifyIfNumInInterval(first_num, last_num, num_to_test, closed_interval=True):
     
    if not closed_interval: 
        testing = first_num + 1
    
        while testing < last_num:

            if testing == num_to_test: 
                return True 

            testing += 1

        return False

    else: 
        testing = first_num
        
        while testing <= last_num:
            
            if testing == num_to_test:
                
                return True 
            
            testing += 1

        return False

conta = verifyIfNumInInterval(2, 8, 8, False)

print(conta)

'''''
Correão ChatGPT:
----------------
def verify_if_num_in_interval(start, end, num_to_test, closed_interval=True):
    if closed_interval:
        return start <= num_to_test <= end
    else:
        return start < num_to_test < end
'''