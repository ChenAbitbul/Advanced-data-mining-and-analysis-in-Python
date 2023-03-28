# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 09:51:39 2023

@author: Hen Abitbul
"""

###################################
# QUESTION 1:
def my_func(x1,x2,x3):
    try:
        if type(x1) != float or type(x2) != float or type(x3) != float:
            if type(x1) != str or type(x2) != str or type(x3) != str:
                return None
            else:
                return "Error: parameters should be float"
        else:
            counter= x2+x3
            deno= x1+x2+x3
            y= (deno*counter*x3)/deno
            return (y)
    except:
        deno= x1+x2+x3
        if deno==0:
            return ("Not a number – denominator equals zero")

###################################
# QUESTION 2:
def revword(word:str) -> str: 
        return word[::-1].lower()


def countword()->int:
    df = open ("text.txt","r")
    word=None
    count_val=1
    for line in df:
        words= line.split()
        for st in words:
            if word== None:
                word=st
            else:
                if word== revword(st):
                    count_val+=1
    return word, count_val
        
print (countword())
            





