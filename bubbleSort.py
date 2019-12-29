#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: /Users/maion/OneDrive/Documentos/Documentos Felipe/programs/ruby/Python/PyCharmProjects/testes/bubbleSort.py
# Project: /Users/maion/OneDrive/Documentos/Documentos Felipe/programs/ruby/Python/PyCharmProjects/testes
# Created Date: Friday, December 20th 2019, 7:46:53 pm
# Author: Felipe Maion
# -----
# Last Modified: Fri Dec 20 2019
# Modified By: Felipe Maion
# -----
# Copyright (c) 2019 MaioneSys
# 
# 
# 
# -----
# HISTORY:
# Date      	By	Comments
# ----------	---	----------------------------------------------------------
###
import timeit

def bubbleSort(nlist):
    for passnum in range(len(nlist)):
        for i in range(passnum):
            if nlist[i][1]>nlist[i+1][1]:
                nlist[i],nlist[1+1] = nlist[i+1],nlist[i]
    return(nlist)



start_time = timeit.default_timer()
nlist = [['a',15], ['g', 25], ['x', 7]]
bubbleSort(nlist)
bubbleSort_time = timeit.default_timer() - start_time

print("WillSort:", bubbleSort_time*1000, "s:", nlist)

start_time = timeit.default_timer()
nlist = [['a',15], ['g', 25], ['x', 7]]
nlist.sort(key= lambda x: x[1])
sort_time = timeit.default_timer() - start_time
print("PythonSort:", sort_time*1000, "s:", nlist)
print("WillSort eh", (bubbleSort_time/sort_time - 1)*100, "% mais lento")