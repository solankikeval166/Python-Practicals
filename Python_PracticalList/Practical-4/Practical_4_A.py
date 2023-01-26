#Defining the function result which shows the grade according to the SGPA
def result(a):
    if a ==10:
        print("Outstanding")
        
    elif a>=9 and a < 10:
        print("Excellent")
        
    elif a>=8 and a<9:
        print("Very good")
        
    elif a>=7 and a<8:
        print("Good")
        
    elif a>=6 and a<7:
        print("Fair")
        
    elif a>=5 and a<6:
        print("Satisfactory")
        
    else:
        print("FAIL")
        
# Calling the function result 
for i in range(5):
    print()
    result(float(input("Please enter Your SGPA:")))    