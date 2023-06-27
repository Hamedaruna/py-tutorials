#creating a program to collect 10 test scores and passing info if more than 6 passes or not


#Create a Function called Rating
def Rating():
    
    #Create variables
    count = 0
    passed = 0
    
    #create while loop to iterate and receive scores 10 times
    while (count <= 10):
        
        #create score variable to collect scores
        score = int(input("Enter Score: ")) 
        
        #create condition to increase passed mark for above 50     
        if (score > 50):
            
            passed+=1
            
        count+=1
     
    #create condition to print message if passed is above or below 6   
    if (passed >= 6):
            
        print("Well Done Instructor.")
        
    else:
        print("Ashi yere!!! LOSER!!!")
 
#call the function (Note: Without calling a function it wouldn't work)       
Rating()