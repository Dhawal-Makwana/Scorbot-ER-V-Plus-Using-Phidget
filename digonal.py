from functions import control

import threading

    
def Fun1():
   
    control(146552,0.5,2)
    
def Fun2():
    control(146680,-0.5,2)
     


    
def Run():
    t1=threading.Thread(target=Fun1)
    t2=threading.Thread(target=Fun2)

    t1.start()
    t2.start()
    t1.join()
    t2.join()
  
    