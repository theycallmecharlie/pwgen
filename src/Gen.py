import random
import pyperclip
import string

class Gen:
    def __init__(self, length):
        self.length = length
    def newpw(self):
        pw = ""
        for char in range(self.length):
            r = random.choice()
            if r < 0.3:
                pw += random.choice(string.punctuation)
            if 0.3 < r < 0.7:
                pw += random.choice(string.ascii_letters)
            if r > 0.7:
                pw += str(random.choice(string.digits))
            pyperclip.copy(pw)
        print(f'\u001b[33m[\u001b[0m+\u001b[33m]\u001b[0m{pw}')
        return print(u"[\u001b[32m+\u001b[0m] \u001b[32mCopied to clipboard.\u001b[0m")
