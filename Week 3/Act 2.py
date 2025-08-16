# Week3- Activity 2: count the words in the demo text file
 
# Develop a new project that reads demo.txt and returns the total number of words. 
# Share the GitHub repository link and a screenshot of the result.
class counting:
    def __init__(self,text):
        self.text=text
    def no_words(self):
        try:
            with open(self.text, "r", encoding="utf-8") as file:
                content = file.read()  # Reads the entire file
                print(content)
                words=content.split()
                total_words=len(words)
                print("Total no of words is :" ,total_words)
        except UnicodeDecodeError:
            print("Cannot decode file: invalid characters detected.")
    def finalfile():
        filepath=r"C:\Users\UD Sec Vaio\OneDrive\Documents\GitHub\MSE800-Uma\Week 3\demo.txt"
        content=counting(filepath)
        content.no_words()
    
if __name__=='__main__':
    counting.finalfile()
