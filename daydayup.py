# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 17:46:25 2020

@author: 杜敬祎
"""
a=eval(input("输入："))
dayup=(1+a)**367
daydown=(1-a)**365
print("向上：{:.2f},向下：{:.2f}".format(dayup,daydown))