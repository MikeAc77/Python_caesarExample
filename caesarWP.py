#!/usr/bin/python3

import sys
import fileinput

#This function receives plaintext and N hops to encrypt text.
def caesarcrypt(plaintext:str,hops:int):
    cryptext=""
    for let in plaintext:
#This will tell me if is either a character or not.}
        if not let.isalpha() :
            cryptext=cryptext+let
            continue
#In order to process characters correctly I need to define their own ascii codes upper/lower..
        if let.isupper() is True:
            baseN=65
        else:
            baseN=97 

#This formula makes the program work with N hops
        finL=((ord(let)-baseN)+hops)%25 
        cryptext=cryptext + chr(finL+baseN)   
    return cryptext


def main(argv,pipetext:str):

#This code prints an error when !=1 arguments are passed.
    if len(argv) != 2: 
        print("Usage:{0} non-neg_integer".format(argv[0]))
        exit(1)

    try:
#it converts str to int
        hops=int(argv[1])
    except Exception as err:
        print("{} cannot be converted to an int, Error {} ".format(sys.argv[1],err))
        exit(2)
#I need to know whether a pipe was read
    if not pipetext :
        plaintext=input("plaintext:")
    else:
        print("plaintext: "+pipetext)
        plaintext=pipetext
    print("cyphertext: {}".format(caesarcrypt(plaintext,hops)))


if __name__ == "__main__":
    pipetext=""
    #to avoid that the  program gets stuck when reading from pipes
    if not sys.stdin.isatty():
        for line in sys.stdin.readlines():
            pipetext=pipetext+line

    main(sys.argv,pipetext[:-1])

    #if not sys.stdin:
        #print(sys.stdin)
    #else:
     #   main(sys.argv)

