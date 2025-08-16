# , open, read, and write
class modifyfile:
    def __init__(self,loc):
        self.loc=loc
    def readfile(self):
        try:
            with open(self.loc, "r", encoding="utf-8") as file:
                content = file.read()  # Reads the entire file
                print(content)
        except UnicodeDecodeError:
            print("Cannot decode file: invalid characters detected.")
    def writefile(self,text):
        try:
            with open(self.loc, "w", encoding="utf-8") as file:
                file.write(text+'\n')  
                print("Text written successfully.")
        except UnicodeDecodeError:
            print("Cannot decode file: invalid characters detected.")

        
    def finalfile():
        filepath=r"C:\Users\UD Sec Vaio\OneDrive\Documents\GitHub\MSE800-Uma\Week 3\demo.txt"
        content=modifyfile(filepath)
        text="This is writing in the new file"
        content.readfile()
        content.writefile(text)
        content.readfile()
if __name__=='__main__':
    modifyfile.finalfile()
    