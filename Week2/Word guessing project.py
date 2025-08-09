import random





def generate_blank():
    blank='_'*len(random_words)
    print('Leaving total blank ',blank,len(random_words))
    return

def checking_user_inputs(timeout):
    
    
    letter = input("User please enter a single letter to guess the random word: ").strip() 
    if letter in random_words:
        total_letter.add(letter)
        print('Letter found here')
        print("total_letter:," ,total_letter)
        result=''.join(c if c in total_letter else'_' for c in random_words )
        print('see the letters', result)        

    else:
        
            print('Sorry no letter matches here , Try Again')
        # timeup=1+timeup
              
        # print(timeup)
    
    return timeout


if __name__ == "__main__":
    words = ["colors", "dress", "laptops", "month", "crew", "product"]
    random_words=random.choice(words)
    total_letter=set()
    timeout=1
    generate_blank()
    while True:
        checking_user_inputs(timeout)
        if timeout>5:
            print('Game Over')
        if   total_letter==set(random_words) :
            print("Found all letters, Congrats")
            break
        else:
            continue
    

