

import logging as ls

ls.basicConfig(filename="C:\\Users\\amit_kumar_singh5\\class_notes\\test\\am23.log",level=ls.INFO)

def mod12(a):
        print(a)
        print(type(a))
        ls.error("checking")
        l=[]
        try:
             for i in range(a):
                if i%2 == 0 and i != 0:
                    l.append(i)
           
        except Exception as e:
            print("some exception ",e)
        else:
            return l
            

         