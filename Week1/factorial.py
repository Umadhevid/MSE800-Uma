def fact(n):
    result=''
    if n>=0:
        result = 1
        for i in range(2, n + 1):
            result *= i
    print ('Factorial for given  ',n,' is ', result)  
    if n<0:
        
        print('Factorial doesnt handle negative number')      
    return result

fact(5)
# if _name_='_main_'

