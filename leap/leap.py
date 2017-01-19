def is_leap_year(year):
    if(not year % 4 == 0):
        print(year , 'is not a leap year.')
        return False
    elif year % 4 == 0 and year % 100 == 0 and not year % 400 == 0:
        print(year , 'is not a leap year.')   
        return False
    else :
        print(year , 'is a leap year.')
        
    return True

if __name__ == '__main__': 
    print (is_leap_year(int(input('Enter year : ')))  )
    
        