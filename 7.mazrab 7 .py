number = int(input('please enter your number'))
if number % 7 == 0:
    print('your number is multiple of 7')

else:
    while number % 7 !=0:
        number=number+1
    print('next multiple of 7:', number)