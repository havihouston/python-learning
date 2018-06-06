# -*- coding: utf-8 -*-
"""
Created on Wed Jun 06 10:53:25 2018

@author: havi
"""

#函数参数传递的问题
#对于不可变对象的使用，比如int str型参数

str1 = 'HAVI'

print id(str1)

def strfun(x = 'None'):
    print 'the adress of x is ' + str(id(x))

    
def strfun1(x = 'None'):
    print id(x)
    x = 'houston'#对于这些不可变得变量，重新赋值就意味着重新开辟一片内存
    print id(x)
    print x

def strfun2(x = 'None'):
    x = x.lower()
    id(x)
    print x

strfun(str1)

print id(str1)

strfun1(str1)

print id(str1)

strfun2(str1)

print id(str1)

#函数参数传递的问题
#对于不可变对象的使用，比如int 
print '####################################################'
num = 12

print id(num)

def strfun(x = 0):
    print 'the adress of x is ' + str(id(x))

    
def strfun1(x = 0):
    print id(x)
    x = 2#对于这些不可变得变量，重新赋值就意味着重新开辟一片内存
    print id(x)
    print x

def strfun2(x = 0):
    x = x.__float__()
    id(x)
    print x

strfun(num)

print id(num)

strfun1(num)

print id(num)

strfun2(num)

print id(num)


#函数参数传递的问题
#对于可变对象的使用，比如list
print '######################################################'
num = [12 , 11 , 10 , 8 , 5]

print id(num)

def strfun(x = []):
    print 'the adress of x is ' + str(id(x))

    
def strfun1(x = []):
    print id(x)
    x = ['tom' , 'candy']#对于这些不可变得变量，重新赋值就意味着重新开辟一片内存
    print id(x)
    print x

def strfun2(x = []):
    x.append('havi')
    id(x)
    print x

strfun(num)

print id(num)

strfun1(num)

print id(num)

strfun2(num)

print id(num)

##############################################################
#the answe is 
#179084064
#the adress of x is 179084064
#179084064
#179084064
#177742752
#houston
#179084064
#havi
#179084064
####################################################
#30310992
#the adress of x is 30310992
#30310992
#30310992
#30311232
#2
#30310992
#12.0
#30310992
######################################################
#177747400
#the adress of x is 177747400
#177747400
#177747400
#175367496
#['tom', 'candy']
#177747400
#[12, 11, 10, 8, 5, 'havi']
#177747400


















