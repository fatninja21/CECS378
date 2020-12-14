# -*- coding: utf-8 -*-
"""
CECS378 2019
Project 2
Name:Wilfredo Mendivil
ID # 
Start Date : 
End Date:
"""
def main():
    message = "F elmb vlr afak'q qoxkpixqb fq yv exka, qexq'p texq zljmrqbop xob clo. Fc vlr afa fq yv exka, vlr pelria obal fq ybzrxpb alfkd fq fk yv exka fp fkbccfzfbkq xka qexq'p tev qefp qbuq fp pl ilkd. Xipl, qefp xppfdjbkq zxiip clo x pjxii mvqelk moldoxj. Lkb txv lc plisfkd qefp fp rpfkd pqofkd.jxhbqoxkp() xka tefib fq fp obzljjbkaba; fq fp klq kbzbppxofiv qeb lkiv lmqflk vlr exsb. Elmb vlr exa crk tlohfkd qefp lrq."
    intab = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" 
    outTab= "DEFGHIJKLMNOPQRSTUVWXYZABCdefghijklmnopqrstuvwxyzabc"
    decrypt = message.maketrans(intab,outTab) 
    print(message.translate(decrypt))  
main()