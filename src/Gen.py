import random
import pyperclip
import string

class Gen:
    def __init__(self, length):
        self.length = length

    def newpw(self):
        pw = ""
        symbols = ['@', '#', '$', '%', '!', '\'', ';', '[', ']',
                   '{', '}', '(', ')', '^', '~', ',', '+', '-',
                   ':', '>', '<', '?', '=', '/', '_', '.', '`',
                   '\\', '?', '*', '&', '|']
        chars = ['a', 'b', 'c', 'd', 'e',
                 'f', 'g', 'h', 'i', 'j',
                 'k', 'l', 'm', 'n', 'o',
                 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z',
                 'A', 'B', 'C', 'D', 'E',
                 'F', 'G', 'H', 'I', 'J',
                 'K', 'L', 'M', 'N', 'O',
                 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
        for char in range(self.length):
            r = random.random()
            if r < 0.3:
                pw += random.choice(symbols)
            if 0.3 < r < 0.6:
                pw += random.choice(chars)
            if r > 0.6:
                pw += str(random.randint(0, 9))
            print(f'\u001b[33m[\u001b[0m+\u001b[33m]\u001b[0m{pw}')
            pyperclip.copy(pw)
        return print(u"[\u001b[32m+\u001b[0m] \u001b[32mCopied to clipboard.\u001b[0m")
