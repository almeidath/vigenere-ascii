list=[' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', 
      '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', 
      '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 
      'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', 
      '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
      'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']
"""
This is a list of 95 characters from 32 to the 126 index of the ASCII table. It will work as a lookup table for the method.
"""

def vigenere(start, frase, key):

  result = ""
  for i in range(len(frase)):
    if frase[i] not in list:
      result+=frase[i]
    else:
      if encrypt == 1:
        result+=list[(list.index(frase[i])+list.index(key[i%len(key)]))%len(list)]
      else:
        result+=list[(list.index(frase[i])-list.index(key[i%len(key)]))%len(list)]
  return result

start=int(input("Would you like to:\n1- Encrypt\n2- Decrypt\n"))
frase=input("Frase: ")
key=input("Key: ")
print(vigenere(start, frase,key))
