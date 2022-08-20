username="fatemehnejatifar"
password='fatemeh1449' 
counter=1
while counter < 4:
     username1=input("please enter your username : ") 
     password1=input("please enter your password: ") 
     if username1==username and password1==password:
          print(" welcome") 
          counter=counter+2
     elif counter == 3:
          print('your account has been locked')
     else:
          print('please try again!')
     
     counter=counter+1
