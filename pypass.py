# encoding=utf8
import sys

from src.Generator import *

def start():
    start = '''
Password Length
Weak    | 0 - 15
Strong  | 16 + 
        '''
    return start
def main():
    try:
        print(start())
        if len(sys.argv) > 1:
            length = int(sys.argv[1])
            pw = Generator(length)
            pw.newpw()
        else:
            length = int(input('Length: '))
            pw = Generator(length)
            pw.newpw()
    except Exception() as error:
        print(f"[!] Error: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
