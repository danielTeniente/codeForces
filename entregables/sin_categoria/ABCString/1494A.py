t = int(input())
for _ in range(t):
    string = input()
    opening = string[0]
    closing = string[-1]
    is_regular = True
    if(opening==closing):
        is_regular = False
    else:
        count_opening = 0
        count_closing = 0
        unknown_char = 0
        for char in string:
            if(char==opening):
                count_opening+=1
            elif(char==closing):
                count_closing+=1
            else:
                unknown_char+=1
        
        open_brackets = 0
        if(count_opening==count_closing+unknown_char):
            for char in string:
                if(char==opening):
                    open_brackets+=1
                else:
                    open_brackets-=1
                if(open_brackets<0):
                    is_regular=False    

                
        elif(count_opening+unknown_char==count_closing):
            for char in string:
                if(char==opening or char!=closing):
                    open_brackets+=1
                else:
                    open_brackets-=1
                if(open_brackets<0):
                    is_regular=False    
            
        else:
            is_regular=False

        


    if(is_regular):
        print('YES')
    else:
        print('NO')