# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 09:44:57 2020

@author: 나
"""

import threading

global vari
vari=1
def test1():
    global vari
    t1_count=1
    for i in range(15):
        vari=vari+1
        t1_count=t1_count+1
        print("1더함"+str(vari))
        print("스레드 1 카운터:"+str(t1_count)+"____")
def test2():
    global vari
    t2_count=1
    for i in range(15):
        vari=vari+2
        t2_count=t2_count+1
        print("2더함"+str(vari))
        print("스레드 2 카운터:"+str(t2_count)+"____")
    
if __name__=="__main__":
    t1=threading.Thread(target=test1)
    t2=threading.Thread(target=test2)
    t1.start()
    t2.start()