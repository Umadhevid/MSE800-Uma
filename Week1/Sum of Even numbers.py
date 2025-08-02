# sum of even numers bet 1 to n, 
# use while loop
# modify for odd numbers as well
# print all even numbers


def even(n):
    result=0
    # print('Find the even numbers from the list')
    
    result=0
    for i in range(2,n+1,2):
        print('The even numbers are',i)
        result=result+i
    print('Sum of even numbers',result)       
        
    return result
def odd(n):
    result=0
    # print('Find the even numbers from the list')
    
    result=0
    for i in range(1,n+1,2):
        print('The odd numbers are',i)
        result=result+i
    print('Sum of odd numbers',result)       
        
    return result

def evenwhile(n):
    result=0
   
    i=2
    while i<n+1:
        print('The even numbers are_while ',i)
        result=result+i
        i=i+2
    print('Sum of even numbers_while',result)      
    return result
def oddwhile(n):
    result=0
    i=1
    while i<n+1:
        print('The odd numbers are_while ',i)
        result=result+i
        i=i+2
    print('Sum of odd numbers_while',result)    

    return result
if __name__ == "__main__":
    even(5)
    odd(5)
    evenwhile(5)
    oddwhile(5)