correct_password = "python123"
attempts = 3 

while attempts > 0 :
    password = input ("enter password : ")
    if password == correct_password:
       print("Access granted")
       break
    
    else:
        attempts -= 1
        print(f"incorrect {attempts} attempts left ")
          
if attempts==0 :
   print("Access denied .too many failed attempts.")
        
 # reset the password add it from this step.
 
reset = input("forgot password ? (yes/no ): ").lower()
    
if reset== "yes" :
        new_pw = input ("enter your new password : ")
        correct_password = new_pw
          
        print("password updated successfully ")
        
elif reset =="no":
    print ("ok ! try again later")
        