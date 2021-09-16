# Vigenère ASCII

Vigenère cipher is a method of encrypting text by using a series of interwoven Caesar ciphers following the character indexes of a key. Originally, only the 26 letters of the alphabet are used, but this code applies the Vigenère cipher logic for 95 characters, including upper and lower case letters, numbers and symbols. All characters from the 33 to the 126 decimal index of the ASCII table.

The user will write a text that they want to encrypt, and must define a key for the encryption. Any character on the text that is not on the list will be left as it is. So ideally, don't use accented letters or things like that.

The key can be any word, number or phrase, as long as all characters are present on the 95 characters of the lookup table list. It can also be any length, the more characters the better, but keep in mind that if the key is longer than the text, the extra characters will be useless for the encryption process.

## Example

Text: Attack the enemy camp at dawn\
Key: lemon\
Result: .ZbQRXebXTlK\U\feQQ\]eOdnQGe^

To decrypt, just select the option, type the encrypted text and enter the original key:

Text: .ZbQRXebXTlK\U\feQQ\]eOdnQGe^\
Key: lemon\
Result: Attack the enemy camp at dawn

## Lookup table
```python
list=[' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', 
      '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', 
      '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 
      'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', 
      '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
      'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']
