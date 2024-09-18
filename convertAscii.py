def convertAscii(text):
    
    encryptList = list(text.encode("ascii")) 
    encryptList = [str(element) for element in encryptList]

    encoded = ''

    for i in range(len(encryptList)):
        if len(encryptList[i]) == 2:
            encryptList[i] = "0" + encryptList[i]

        elif len(encryptList[i]) == 1:
            encryptList[i] = "00" + encryptList[i]
            
        

        encoded += encryptList[i]
    return encoded