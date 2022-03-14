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
                    '0':'-----'}

def check(inp):
    for i in inp[1:]:
        for x in i:
            if not x == ' ' and not x.isalnum():
                return False
    return True
# morse = ''
if len(sys.argv) > 1:
    inp = sys.argv
    if check(inp) == False:
        print("ERROR")
    else:
        for i in inp[1:]:
            for x in i:
                if x.upper() in MORSE_CODE_DICT:
                    print(MORSE_CODE_DICT[x.upper()], end=' ')
                    # morse += MORSE_CODE_DICT[x.upper()] + ' '
                elif x == ' ':
                    print('/', end=' ')
                    # morse += '/ '
            if i != inp[-1]:
                print('/', end=' ')
                # morse += '/ '
        print() 
    # print(morse)
