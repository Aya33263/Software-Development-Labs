#age verification  edit

age=int(input("enter your age :"))

if age <=0 :
    print ("error")

elif age >=65:
    print ("senior citizens")

elif age >=18 :
    print ("you are eligible to vote")  

else :
    print("you are not eligible to vote")