lis = [[3,5,10,8],2,5,6,2,3,5,[2,5,3,5],7,10,9,20,15,13,25,30,24]


print (lis)
print (len(lis))
print ("NEW")
rev = []
for i in range (len(lis),-1,-1):

    rev.append(lis[i])

print (rev)
print ('this is the length of rev', len(rev))