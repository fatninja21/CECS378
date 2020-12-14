# -*- coding: utf-8 -*-
"""
CECS378 2019
Project 2
Name:Wilfredo Mendivil
ID # 017471907
Start Date : 
End Date:
"""
def main():
    decipherMessage = ("F elmb vlr afak'q qoxkpixqb fq yv exka, qexq'p texq zljmrqbop xob clo. Fc vlr afa fq yv exka, vlr pelria obal fq ybzrxpb alfkd fq fk yv exka fp fkbccfzfbkq xka qexq'p tev qefp qbuq fp pl ilkd. Xipl, qefp xppfdjbkq zxiip clo x pjxii mvqelk moldoxj. Lkb txv lc plisfkd qefp fp rpfkd pqofkd.jxhbqoxkp() xka tefib fq fp obzljjbkaba; fq fp klq kbzbppxofiv qeb lkiv lmqflk vlr exsb. Elmb vlr exa crk tlohfkd qefp lrq.")
    key = 23
    print(TranslateMessage(key, decipherMessage))
def TranslateMessage(key,message):
    decrypt = ''
    for characterType in message:
        if characterType.isalpha():
            
             #num = ord(characterType)
             #num = num - key
             #print(num)
             if characterType.isupper():
                 num = ord(characterType.lower())
                 num = num - key
                 if num< ord('a'):
                    num = num +26
                    #characterType.capitalize
                    characterType = chr(num)
                    num =  ord(characterType.upper())
                 if num == ord('a'):
                    characterType = chr(num)
                    num = ord(characterType.upper())
             elif characterType.islower():
                 num = ord(characterType)
                 num = num - key
                 if num< ord('a'):
                    num = num +26

                    #num =chr(num)
             decrypt += chr(num)
        else:
            decrypt += characterType
    return decrypt    
main()