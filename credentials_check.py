user_name = input("Enter the user name : ")
if '@' in user_name:
 
    password = input("Enter the Password : ")

#Case 1 : Both are Correct 
    if user_name == "arnab7084@gmail.com" and password == "1994":
        print ("Correct Credentials - You're Welcome")
    
#Case 2 : User Name correct and Password wrong 
    elif user_name == "arnab7084@gmail.com" and password != "1994":
    
        print ("User Name is correct , but Password is wrong")
        password = input("Enter the Password : ")
    
        if password == "1994":
            print ("Correct Password - You're Welcome")
       
        else:
            print ("Incorrect Credentials")
 
#Case 3 : User Name wrong and Password correct 
    elif user_name != "arnab7084@gmail.com" and password == "1994":
    
        print ("User Name is wrong , but Password is correct")
        user_name = input("Enter the User name again : ")
    
        if user_name == "arnab7084@gmail.com":
            print ("Correct User Name - You're Welcome")
       
        else:
            print ("Incorrect Credentials")
        
        
#Case 4 : Both User Name and Password are Incorrect 
    elif user_name != "arnab7084@gmail.com" and password != "1994":
    
        print ("Both User Name and Password are Incorrect ")
        user_name = input("Enter the User name again : ")
        password = input("Enter the Password again : ")
    
        if user_name == "arnab7084@gmail.com" and password == "1994":
            print ("Correct Cedentials - You're Welcome")
       
        else:
            print ("Incorrect Credentials")
        
else:
    print ("The user name entered is incorrect ! ")