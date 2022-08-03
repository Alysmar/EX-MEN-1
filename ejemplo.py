import gc
import ctypes
import sys


class Node:
  def __init__(self, value):
    self.value = value
  def child(self,child):
    self.child=child  
    
    
A= Node("A")
B=Node("B")
C=Node("C")  

A.child(B)
B.child(C)
C.child(B) 

print(sys.getrefcount(A))
print(sys.getrefcount(B))
print(sys.getrefcount(C))

del A

i = 0 
def creando_ciclos(): 
    x = { } 
    x[i+1] = x 
    print(x) 
    
print ("Creando ciclos...")
for i in range(10): 
    creando_ciclos()   

print("Umbrales de recolección de basura:", gc.get_threshold())
print("conteo de referencias:", gc.get_count())
gc.set_debug(gc.DEBUG_SAVEALL)
collected= gc.collect()
print(gc.garbage)
print("Garbage collector: collected", "%d objects." % collected)
print("conteo de referencias:", gc.get_count())
