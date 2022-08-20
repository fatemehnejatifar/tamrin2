final_score = 0 
equal = 0 
winner = 0 
loser = 0 
Counter = 1
while (Counter < 9): 
    print ('emtiaz mosabegheh :', Counter ,'ra vared konid: ') 
    score = int(input()) 
    if ((score == 0) or (score == 3)): 
        final_score =final_score + score 
        Counter += 1 
        if (score == 3): 
            winner += 1 
        elif (score == 1): 
            equal += 1 
        elif (score == 0): 
            loser += 1 
        else: print('vorodi shoma khata darad !') 
        
print ('final_score winner equal loser ',' ',final_score,' ',winner,' ',equal,' ',loser)