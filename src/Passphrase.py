# encoding=utf8
#!/usr/bin/python3
import random
import pyperclip
from src.Timer import *


class Passphrase:
    def __init__(self, length, verbose):
        self.length = length
        self.verbose = verbose

    def passphrase(self):
        passphrase = ''
        with open('wl.txt', 'r') as f:
            words = f.readlines()
            f.close()
        for i in range(self.length):
            passphrase += random.choice(words).replace("\n", " ")
        print(f"{Color.WHITE}[{Color.GREEN}+{Color.WHITE}]{Color.GREEN} Passphrase generated.{Color.WHITE}")
        pyperclip.copy(passphrase)
        print(f"{Color.WHITE}[{Color.GREEN}+{Color.WHITE}]{Color.GREEN} Copied to clipboard.{Color.WHITE}", end="\n")
        print(f"[{Color.BLUE}Passphrase{Color.WHITE}]: {passphrase}{Color.WHITE}", end="\n")
        Timer.graph()
        return print(f"{Color.WHITE}[{Color.HEADER}-{Color.WHITE}] Clipboard cleared.")
