class StringManipulator:
    def __init__(self,text):
        self.text=text
    def find_character(self,char):
        return self.text.find(char)
    def string_length(self):
        return len(self.text)
    def convert(self):
        return self.text.upper()

def main():
    name=StringManipulator("sunDay")
    result=name.find_character('a')
    length=name.string_length()
    convert=name.convert()
    print('Character found in place',result)
    print('String Length',length)
    print('String Converted in to Upper case',convert)
    # string's length and convert it to uppercase.

if __name__=="__main__":
    main()

