from convertAscii import convertAscii

textToEncrypt = "abcdefg"

key = 'ajenkbaba'

encoded = convertAscii(textToEncrypt)
encodedKey = convertAscii(key)


print(int(encodedKey) * int(encoded) )