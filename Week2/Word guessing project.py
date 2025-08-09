import random

def generate_blank():
    blank='_'*len(random_words)
    print('Leaving total blank ',blank,len(random_words))
    return

def checking_user_inputs():
    
    
    letter = input("User please enter a single letter to guess the random word: ").strip() 
    if letter in random_words:
        total_letter.add(letter)
        print('Letter found here')
        print("total_letter:," ,total_letter)
        result=''.join(c if c in total_letter else'_' for c in random_words )
        print('see the letters', result)   
        timeout=0     

    else:
        print('Sorry no letter matches here , Try Again')
            
    
    return 


if __name__ == "__main__":
    words = ["colors", "dress", "laptops", "month", "crew", "product"]
    random_words=random.choice(words)
    total_letter=set()
    timeout=0
    generate_blank()
    while True:
        checking_user_inputs()
        if timeout!=0 and timeout>5:
            print('Game Over')
            break
        else:
            timeout=1+timeout
        if   total_letter==set(random_words) :
            print("Found all letters, Congrats")
            break
        else:
            continue
    

