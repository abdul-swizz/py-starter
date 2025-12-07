from array import *

names = array( 'i',[5, 6, 8, 2, 3, 10, 7,20,60,30])

new = array('i', (a for a in names))

print (len(names), 'is the length of the names array' .upper() )
print (new, 'this is new array')

i = 0
while i <= (len(names)-1):
    print (new[i])
    i += 1
