#!/usr/bin/python3

import sys

#This function receives plaintext and N hops to encrypt text.
def caesarcrypt(plaintext:str,hops:int):
    cryptext=""
    for let in plaintext:
#This will tell me if is either a character or not.}
        if not let.isalpha():
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


def main(argv):
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

    plaintext=input("plaintext:")
    print("cyphertext: {}".format(caesarcrypt(plaintext,hops)))


if __name__ == "__main__":
    main(sys.argv)

