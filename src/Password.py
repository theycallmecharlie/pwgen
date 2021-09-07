# encoding=utf8
#!/usr/bin/python3
import random
import pyperclip
import string
from src.Timer import *
from src.Color import *


class Password:
    def __init__(self, length, verbose):
        self.length = length
        self.verbose = verbose

    def newpw(self):
        password = ""
        for i in range(self.length):
            punctuation, digit, ascii = random.choice(string.punctuation), random.choice(string.digits), random.choice(string.ascii_letters)
            password += random.choice([punctuation, digit, ascii])
        print(f"{Color.WHITE}[{Color.GREEN}+{Color.WHITE}]{Color.GREEN} Password generated.{Color.WHITE}")
        pyperclip.copy(password)
        print(f"{Color.WHITE}[{Color.GREEN}+{Color.WHITE}]{Color.GREEN} Copied to clipboard.{Color.WHITE}", end="\n")
        if(self.verbose):
            print(f"[{Color.BLUE}Password{Color.WHITE}]: {password}{Color.WHITE}", end="\n")
        Timer.graph()
        return print(f"{Color.WHITE}[{Color.HEADER}-{Color.WHITE}] Clipboard cleared.")
