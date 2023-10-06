# ASCII Art Encoding
# Write a function "encodeString" that will encode a string like 'AAAAABBBBAAA' as a list of tuples: [('A', 5), ('B', 4), ('A', 3)] 
# meaning that the string has "5 A's, followed by 4 B's, followed by 3 A's"

# Then use that function to compress a string containing "ASCII Art" (https://en.wikipedia.org/wiki/ASCII_art)

# Write a corresponding function "decodeString" that will take in a list of tuples and print the original string.

def encodeString(stringVal):
    listOfTuple = []   
    prevchr = stringVal[0]
    count = 0
    for chr in stringVal:
        if prevchr != chr:
            listOfTuple.append((prevchr, count))
            count = 0
        prevchr = chr
        count += 1
    listOfTuple.append((prevchr, count))
    return listOfTuple

def decodeString(encodedList):
    stringResult = ""
    for chr, qtd in encodedList:
        stringResult += chr * qtd
    return stringResult


 # 'AAAAABBBBAAA' as a list of tuples: [('A', 5), ('B', 4), ('A', 3)] 

stringVal = 'AAAAABBBBAAA'
encodedList = encodeString(stringVal)
print("encodeString: ",encodedList)

decodedStr = decodeString(encodedList)
print("decodeString: ", decodedStr)

print("Encode and Decode Smile Art")

art = '''

                                                                                
                                                                                
                               %%%%%%%%%%%%%%%%%%%                              
                        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                       
                    %%%%%%%%                         %%%%%%%%                   
                %%%%%%%                                   %%%%%%                
              %%%%%%                                         %%%%%%             
           %%%%%%                                               %%%%%           
          %%%%%                                                   %%%%%         
        %%%%%                                                       %%%%%       
       %%%%                 %%%%%              %%%%%                  %%%%      
      %%%%                 %%%%%%%            %%%%%%%                  %%%%     
     %%%%                  %%%%%%%            %%%%%%%                   %%%%    
    %%%%                   %%%%%%%            %%%%%%%                    %%%%   
    %%%%                    %%%%%              %%%%%                     %%%%   
   %%%%                                                                   %%%%  
   %%%%                                                                   %%%%  
   %%%%                                                                   %%%%  
   %%%%                                                      %%%%        %%%%   
    %%%%       %%%%%%                                        %%%%%       %%%%   
    %%%%         %%%%                                       %%%%        %%%%    
     %%%%         %%%%                                     %%%%         %%%%    
      %%%%         %%%%%                                  %%%%         %%%%     
       %%%%%         %%%%%                             %%%%%         %%%%%      
        %%%%%          %%%%%%                        %%%%%          %%%%        
          %%%%%           %%%%%%%               %%%%%%%           %%%%%         
            %%%%%             %%%%%%%%%%%%%%%%%%%%%             %%%%%           
              %%%%%%%                                        %%%%%              
                 %%%%%%%                                 %%%%%%%                
                     %%%%%%%%%                     %%%%%%%%%                    
                          %%%%%%%%%%%%%%%%%%%%%%%%%%%%%                         
                                   %%%%%%%%%%%%                                 
                                                                                
                                                                                 

'''

encodedList = encodeString(art)
print("encodeString: ",encodedList)

decodedStr = decodeString(encodedList)
print(decodedStr)

