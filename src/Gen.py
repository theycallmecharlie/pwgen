import random
import pyperclip
import string

class Gen:
    def __init__(self, length):
        self.length = length

    def newpw(self):
        pw = ""
        for char in range(self.length):
            r = random.random()
            if r < 0.3:
                pw += random.choice(string.punctuation)
            if 0.3 < r < 0.6:
                pw += random.choice(string.ascii_letters)
            if r > 0.6:
                pw += str(random.choice(string.digits))
            #print(f'\u001b[33m[\u001b[0m+\u001b[33m]\u001b[0m{pw}')
            pyperclip.copy(pw)
        print(f"Pw: {pw}")
        return print(u"[\u001b[32m+\u001b[0m] \u001b[32mCopied to clipboard.\u001b[0m")
