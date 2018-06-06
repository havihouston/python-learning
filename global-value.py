# -*- coding: utf-8 -*-
"""
Created on Wed Jun 06 11:47:35 2018

@author: havi
"""
x = 10
print id(x)
print x
print '#################################'

def setx(y):
    x = y
    print id(x)
    print x
    
setx(5)
print id(x)
print x

print '#################################'
def sety(y):
    global x
    x = y
    print id(x)
    print x
    
setx(5)
print id(x)
print x

print '#################################'

sety(5)
print id(x)
print x
    
 