import sys

def filterwords(string, number):
    word = ""
    number = int(number)
    string_list = []
    for i in range(len(string)):
        if(string[i] != " "):
            word += string[i]
        elif(string[i] == " " or string[i] == string[len(string) - 1]):
            string_list.append(word)
            word = ""
    string_list.append(word)
    words = []
    for word in string_list:
        print(word, len(word))
        if len(word) > number:
            words.append(word)
    return words
            
            


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("ERROR")
    else:
        print(filterwords(sys.argv[1], sys.argv[2]))
            