counter = 0 
while counter != 1: 
    first_meghyas = input('plesae choose your convert type from "F", "C", "K": ') 
    second_meghyas = input('plesae choose the temperature unit from "F", "C", "K":') 
    if ((first_meghyas == 'F') or (first_meghyas == 'C') or (first_meghyas == 'K')) and ((second_meghyas == 'F') or (second_meghyas == 'C') or (second_meghyas == 'K')) and first_meghyas != second_meghyas: 
        meghyas = int(input('please enter temprature: ')) 
        counter = 1 
    else: 
        print('meghyas dama bayad az bein "F", "C", "K" bashad') 

if  first_meghyas == 'C': 
    if second_meghyas == 'F': 
        meghyas = (meghyas * 9 / 5) + 32 
        print('temprature to farenheit: ', meghyas) 

    elif second_meghyas == 'K': 
        meghyas = (meghyas + 273.15) 
        print('temprature to kelvin ', meghyas) 

elif   first_meghyas == 'F': 
    if second_meghyas == 'C': 
           meghyas = (meghyas - 32) * 5 / 9 
           print('temprature to celciuse: ', meghyas)
    elif second_meghyas == 'K': 
           meghyas = (meghyas - 32) * 5 / 9 + 273.15 
           print('temprature to kelvin: ', meghyas) 
elif first_meghyas == 'K': 
    if second_meghyas == 'C': 
           meghyas = (meghyas - 273.15) 
           print('temprature to celsius: ', meghyas) 
    elif second_meghyas == 'F': 
           meghyas = (meghyas - 273.15) * 9 / 5 +32 
           print('dama be farenheit: ', meghyas)