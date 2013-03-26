import sys
import math

## Global variable BLOCKSIZE = 8
BLOCKSIZE = 8

def input_encrypt(text, key):
    #Actually I am overwriting the that has been calling from main
    user_input = raw_input("Enter the key you want to use, should be 8 digit [don't to put anything new, press enter]: ").strip()
    if user_input!="":
        key = user_input
    else:
        key=key
    
    value = len(text)
    output = ""
    full_frag = value/BLOCKSIZE
    partial_frag = value%BLOCKSIZE
    adder = 0
    if partial_frag > 0:
        adder = 1
    text = (("0")*(BLOCKSIZE-partial_frag)) + text

    if adder == 1:
        temp = code_block(text[(BLOCKSIZE-partial_frag):partial_frag], key[(BLOCKSIZE-partial_frag):partial_frag])
        output += temp
    for i in range(full_frag):
        initial = text[((i+1)*BLOCKSIZE):(((i+2)*BLOCKSIZE))]
        temp = code_block(initial, key)
        output += temp
    return output
        
def decrypt(text, key):
    user_input = raw_input("Enter the key you want to use, should be 8 digit [don't to put anything new, press enter]: ").strip()
    if user_input!="":
        key = user_input
    else:
        key=key
    value = len(text)
    output = ""
    full_frag = value/BLOCKSIZE
    partial_frag = value%BLOCKSIZE
    adder = 0
    if partial_frag > 0:
        adder = 1
    text = (("0")*(8-partial_frag)) + text

    if adder == 1:
        temp = decode_block(text[(BLOCKSIZE-partial_frag):partial_frag], key[(BLOCKSIZE-partial_frag):partial_frag])
        output += temp
    for i in range(full_frag):
        initial = text[((i+1)*BLOCKSIZE):(((i+2)*BLOCKSIZE))]
        temp = decode_block(initial, key)
        output += temp
    return output

    
def decode_block(n, key):
    output = ""
    n=n.strip()
    key=key.strip()
    for i in range(len(n)):        
        temp = decode_digit(int(n[i]), int(key[i]))
        output += str(temp)    
    return str(output)

def code_block(n, key):
    output = ""    
    for i in range(len(n)):        
        temp = code_digit(int(n[i]), int(key[i]))
        output += str(temp)    
    return str(output)

def unkey(key):
    temp = ""
    for i in range(BLOCKSIZE):
        val = undo(int(key[i]))
        temp += str(val)
    return temp
    
def undo(key):
    if key==0:
        return 0
    else:        
        return (10-key)

def decode_digit(n, key):
    if key==0:
        val = key
    else:
        val = 10 - key
    return (n + val)%10
    
def code_digit(n, key):
    return (n+key)%10

def block(text):
    return text[-BLOCKSIZE:]

def rest(text):
    return text[:-BLOCKSIZE]

def main():
    result = input_encrypt('1234567890123456789012','11223344')
    sys.stdout.write( 'Encoded value: %s' % result )
    sys.stdout.flush()
    print "\n"
    new_result = decrypt('3467908912457867902356','12345678')
    sys.stdout.write( 'Decoded value: %s' % new_result )
    sys.stdout.flush()

main()
