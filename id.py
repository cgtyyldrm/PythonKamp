a = [300]
b = [300]
c = [300]
print (id (300))
print (id (a))
print (id (b))
print (id (c))

a = b
b = c
print (id (300))
print (id (a))
print (id (b))
print (id (c))

a = b = c
print (id (300))
print (id (a))
print (id (b))
print (id (c))