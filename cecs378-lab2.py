# -*- coding: utf-8 -*-
"""
CECS378 2019
Project 2
Name:Wilfredo Mendiil
ID # 017471907
Start Date : 
End Date: 9/29/19
"""
#import maketrans   # Required to call maketrans function.
def main():
    encryptedMessage = ("F elmb vlr afak'q qoxkpixqb fq yv exka, qexq'p texq zljmrqbop xob clo. Fc vlr afa fq yv exka, vlr pelria obal fq ybzrxpb alfkd fq fk yv exka fp fkbccfzfbkq xka qexq'p tev qefp qbuq fp pl ilkd. Xipl, qefp xppfdjbkq zxiip clo x pjxii mvqelk moldoxj. Lkb txv lc plisfkd qefp fp rpfkd pqofkd.jxhbqoxkp() xka tefib fq fp obzljjbkaba; fq fp klq kbzbppxofiv qeb lkiv lmqflk vlr exsb. Elmb vlr exa crk tlohfkd qefp lrq.")
    key = 23
    print(TranslateMessage(key, encryptedMessage))
def TranslateMessage(key,message):
    decrypt = '' # empty string in order to fill in with 
    for characterType in message: # itterate through string until it is done
        if characterType.isalpha():# check if chr is a letter
             num = ord(characterType)
             num = num - key  # make num equal to ascii value of char - key
             if characterType.isupper(): # check if char is upper case
                 if num< ord('A'):
                    num = num +26
             elif characterType.islower():# check if character is lower case
                if num < ord('a'):
                    num = num +26 # add 26 back to num in order to get the new value                    
             decrypt += chr(num) # add new decrypted char to string
        else:# character is a symbol or space
            decrypt += characterType # add symbol/space to decrypt string
    return decrypt    
main()
