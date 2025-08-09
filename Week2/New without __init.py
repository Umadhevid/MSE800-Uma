class StringManipulator:
   

    def find_character(name,char):
        return name.find(char)
    def string_length(strings):
        return len(strings)
    def convert(strings):
        return strings.upper()

def main():
    name='sunDay'
    result=StringManipulator.find_character(name,'a')
    print('Character found in place',result)
    print('String Length',StringManipulator.string_length(name))
    print('String Converted in to Upper case',StringManipulator.convert(name))
    

if __name__=="__main__":
    main()

