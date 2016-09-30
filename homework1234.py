
try:
    datafile = open("climdata.txt", "r")
except:
    print ("Sorry the file does not exist.")
else:

    info = dict()

    for line in datafile:
  
        if "Hour" in line:
            continue
        else:
          

           
            time = line[:8]
           
            line.split()
           
            temp = line[10:14]       
            info[time]= temp

    for num in info:
       
        answer = max(info, key=info.get)
        
  
    print ("The highest temperature of",info[answer], "farenheit", "occured at", answer)

    datafile.close()




    




       
   
