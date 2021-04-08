import string

def text_analyzer(text = ""):
    uppers = 0
    lowers = 0
    punctuations = 0
    space = 0
    for i in text:
        if i == " ":
            space += 1
        elif i.isupper():
            uppers += 1
        elif i.islower():
            lowers += 1
        elif i in string.punctuation:
            punctuations += 1
    if text == "":
        text = input("What is the text to analyse?\n")
        return text_analyzer(text)
            
    print("The text contains " + str(len(text)) + " characters:")
    print("- " + str(uppers) + " upper letters")
    print("- " + str(lowers) + " lower letters")
    print("- " + str(punctuations) + " punctuation marks")
    print("- " + str(space) + " spaces")
