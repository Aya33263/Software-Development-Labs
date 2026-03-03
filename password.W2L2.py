correct_password = "python123"
attempts = 3 

while attempts > 0 :
    password = input ("enter password : ")
    if password == correct_password:
       print("Access granted")
       break
    else :
        attempts -= 1
        print(f"incorrect {attempts} attempts left ")
         
if attempts ==0:        
    print("Access denied .too many failed attempts.")
        
      