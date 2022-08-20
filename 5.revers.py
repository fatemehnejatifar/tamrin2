number = int(input('addad khod ra vared konid: ')) 
reversed_number = 0
new_number = number 

while new_number != 0: 
    reversed_number = new_number % 10 + (10 * reversed_number) 
    new_number //= 10

if number == reversed_number: 
    print('addad ba makos an barabar hast')

else:
     print('addad ba makos an barabar nist')