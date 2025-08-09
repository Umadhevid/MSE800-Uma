# Develop a project using class and methods to get a sentence from user input and find the number of words in it. Share your GitHub link at the end.

class sentence:
    def __init__(self,text):
        self.text=text
    def sentence_input(self):
        self.text=input('Enter a sentence:  ')
        return
    def word_count(self):
        words=(self.text)
        words = words.split()
        return len(words)

def main():
    sentence_obj=sentence("")
    input_user=sentence_obj.sentence_input()
    words_count=sentence_obj.word_count()
    print('Number of words in a sentence is : ',words_count)


if __name__=='__main__':
    main()
