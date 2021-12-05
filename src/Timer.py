# encoding=utf8
#!/usr/bin/python3
import time
import pyperclip

from src.Color import *


class Timer():
    def __init__(self) -> None:
        pass

    def graph():
        a = ''        
        for i in range(30,0,-1):
            print(f"{Color.WHITE}[{Color.ALERT}!{Color.WHITE}]{Color.ALERT} Clearing the clipboard in {i} seconds.{Color.WHITE}", end='\r')
            time.sleep(1)
            a += f'{Color.DANGER}█{Color.WHITE}'
        print("")
        pyperclip.copy('')
