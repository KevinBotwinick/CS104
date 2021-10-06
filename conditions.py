temp = int(input('Please enter the current temperature or 999 to end: '))
while(temp !=999):
    if(temp > 90):
        print ('Wear Shorts')
    elif(temp > 70):
        print ('Short sleeves are fine')
    elif (temp > 50):
        print ('Wear a jacket')
    elif (temp > 32):
        print('Wear a heavy coat')
    else:
        print('stay inside')
    temp = int(input('Please enter the current temperature or 999 to end: '))
        
    

        
    




