#encoding=utf8
#!/usr/bin/python3
import argparse
import sys
import string

from src.Gen import *

def main():
    parser = argparse.ArgumentParser(description = 'Simple secure password generator')
    parser.add_argument('-l', '--length', help = 'Define password length, if not flagged, the default length is 16 chars', type = int, default = 16)
    #parser.add_argument('-p', '--password', help = 'Generate a password', action = 'store_true')
    #parser.add_argument('-s', '--symbols', help = 'Exclude special characters to password', action = "store_true", default = False)
    #parser.add_argument('-n', '--numbers', help = 'Exclude numbers to password', action = "store_true", default = False)
    #parser.add_argument('-v', '--verbose', help = 'It provides additional details', action = "store_true", default= False)
    args = parser.parse_args()  
    gen = Gen(args.length)
    gen.newpw()
    
if __name__=='__main__':
    main()