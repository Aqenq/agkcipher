from convertAscii import convertAscii
encrpytedText = "9428817828813616653681814907100256615803997991"
key = "ajenkbaba"

encodedKey = convertAscii(key)

decodedText = str(int(encrpytedText) // int(encodedKey))


if len(decodedText) % 3 == 2:
    decodedText = "0" + decodedText
elif len(decodedText) % 3 == 1:
    decodedText = "00" + decodedText
    
finaltext = ""    

for i in range(0,len(decodedText),3):
    finaltext += chr(int(decodedText[i:i+3]))
    
print(finaltext)