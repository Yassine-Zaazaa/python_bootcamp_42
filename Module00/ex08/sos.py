import sys

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ' ': ' / ' }

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("ERROR")
    else:
        def morse_translate():
            KEYS = list(MORSE_CODE_DICT.keys())
            LIST = sys.argv[1:]
            characters = ""
            for word in LIST:
                for character in word:
                    if character.upper() in KEYS:
                        characters += MORSE_CODE_DICT[character.upper()]
                    else:
                        print("ERROR")
                        return
                    characters += " "
                characters += '/'
            characters = characters[:-2] 
            print(characters)
        morse_translate()
                    