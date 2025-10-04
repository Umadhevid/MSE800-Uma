"""Project to count words in a user-input sentence using a class."""
class Sentence:
    """Class to handle sentence input and word count."""
    def __init__(self,text):
        self.text=text    
    def sentence_input(self):
        """Get sentence from user input."""
        self.text=input('Enter a sentence:  ')          
    def word_count(self):
        """Return the number of words in the sentence."""
        words=(self.text)
        words = words.split()
        return len(words)
def main():
    """Main function to run the sentence analyzer."""
    sentence_obj=Sentence("")
    words_count=sentence_obj.word_count()
    print('Number of words in a sentence is : ',words_count)    
if __name__=='__main__':
    main()

