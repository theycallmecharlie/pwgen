#encoding=utf8
#!/usr/bin/python3
import argparse
import platform
import sys
import os
from src.Color import *
from src.Password import *
from src.Passphrase import *

def main():
    parser = argparse.ArgumentParser(description = "Simple secure password generator")
    parser.add_argument('-pw', '--password', help = 'Generate a password', action = 'store_true')
    parser.add_argument('-pp', '--passphrase', help = 'Generate a passphrase w/ N words, the default is 8 words', action = 'store_true')
    parser.add_argument('-l', '--length', help = 'Define password length, if not flagged, the default length is 8 chars', type = int, default = 8)
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()
    if(args.password): 
        gen = Password(args.length,args.verbose)
        gen.newpw()
    if(args.passphrase): 
        gen = Passphrase(args.length,args.verbose)
        gen.passphrase()
    
if __name__=='__main__':
    if sys.platform == 'linux': 
        import apt
        pkg = apt.Cache()
        if pkg['xclip'].is_installed: pass
        else:
            print(f"[{Color.ALERT}!{Color.WHITE}]{Color.ALERT}You don't have 'xclip' package to copy clipboard{Color.WHITE}")
            try: os.system("sudo apt-get install xclip")
            except Exception as err: print(f"Error: {err}")
    try:main()
    except KeyboardInterrupt: print("PWgen has been stopped")
    except Exception as err: print(f"Error: {err}")