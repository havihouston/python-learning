# -*- coding: utf-8 -*-
"""
Created on Wed Jun 06 16:49:28 2018

@author: havi
"""

#function are object 
#you can used it as :
#assigned to a variable
#an item in a list (or any collection)
#passed as an argument to another function

def febonaci(a=0 , b=1):
    while b < 1000:
        a , b = b , a+b
        print b
        

febonaci(); 