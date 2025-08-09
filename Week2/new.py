class StringManipulator:
    def __init__(self,text):
        self.text=text
    def find_character(self,char):
        return self.text.find(char)
    def string_length(self):
        return len(self.text)
    def convert(self):
        return self.text.upper()
name=StringManipulator("sunDay")
result=name.find_character('a')
length=name.string_length()
convert=name.convert()
print(result)
print(length)
print(convert)
# string's length and convert it to uppercase.