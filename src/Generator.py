# encoding=utf8
import random
import pyperclip


class Generator:
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
            pyperclip.copy(pw)
        return print("[+] Copied to clipboard")
