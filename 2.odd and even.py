fard=0
zoj=0
number= int(input('addad khod ra vared konid :'))

while (number)!=0:
    n=(number%10)
    if ((n%2)==0) or (n==0):
         zoj=zoj+1
    else:
         fard=fard+1

    number=number//10

if(fard>zoj):
    print('tedad ragham fard bishtar hast')

elif(fard==zoj):
    print('tedad ragham fard ba tedad ragham zoj barabar hast')

else:
    print('tedad ragham zoj bishtar hast')

    

