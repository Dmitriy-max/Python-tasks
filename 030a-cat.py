#!/usr/bin/python
import sys
try:
        std_argvLen = len(sys.argv)
        if std_argvLen != 2 :
                print("Incorrect input")
                sys.exit(1)
        
        inputFile =  sys.argv[len(sys.argv) - 1]
        with open(inputFile,'rb') as file:
                
                while True:
                        line = file.read(51200)
                        if len(line) == 0:
                                break
                        sys.stdout.buffer.write(line)
except FileNotFoundError: 
        print("No such file or directory", file=sys.stderr)
        sys.exit(2)
except IsADirectoryError: 
        print("Is a directory", file=sys.stderr)
        sys.exit(3)
except IOError: 
        print("No file", file=sys.stderr)
        sys.exit(4)
except MemoryError: 
        print("Large file size", file=sys.stderr)
        sys.exit(5)








