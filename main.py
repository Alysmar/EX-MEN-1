import sys 
import gc



#print(gc.get_count())

#print(gc.collect())
#print(gc.get_count())


#b=9

#b=4




print("Umbrales de recolección de basura:", gc.get_threshold())

print(gc.get_count())


collected= gc.collect()

print("Garbage collector: collected", "%d objects." % collected)


	

print("creando ciclos...")
x={}
for i in range(10):
	x[i+1]=x
	print(x)
	


#print(lista)




print(gc.is_tracked(x))
print(gc.get_count())

print("recuento de referencias del objeto:", sys.getrefcount(x))
print("Umbrales de recolección de basura:", gc.get_threshold())

print(gc.get_count())

collected= gc.collect()

#print(gc.get_objects())

print("Garbage collector: collected", "%d objects." % collected)


print(gc.get_count())




