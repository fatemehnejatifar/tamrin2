height = float (input('lotfan ghad khod ra be metr vared konid = ')) 
weight = float (input('lotfan vazn khod ra be kilograms vared konid= ')) 
bmi = weight / (height ** 2) 
if 16 > bmi: 
    print ('vazn v ghad shoma normal hast. ')

elif 16 < bmi <= 18.5: 
    print ('shoma kambod vazn darid. ') 

elif 18.5 < bmi <= 24: 
    print ('vazn shoma normal hast. ') 
    
elif 24 < bmi <= 30:
     print ('ghad shoma ideal hast. ') 

elif 30 < bmi <= 35: 
    print('shoma  ezafe vazn darid.') 

elif 35 < bmi <= 40: 
    print ('your are overweight.') 

elif 40 < bmi: 
    print ('shoma ezafe vazn ziyad darid.')