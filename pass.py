#!/bin/env python3

import random
import string
import sys

# use upper and lower less the letter "o|O" (oscar)
lower = string.ascii_lowercase.replace("o", "")
upper = string.ascii_uppercase.replace("O", "")

elements = (lower + upper + string.digits + string.punctuation)


def generate_sequence(length, elements=elements):
    '''
    Generate a sequence of random characters; 1st char must be a lettter
    '''
    while True:
        try:
            first = random.choice(elements)
            assert first.isalpha()
        
        except AssertionError:
            pass
          
        else:
            break
        
        # random.sample returns a list
        last = random.sample(elements, length-1)
        
        return first + ".join(last)

      
def main():
    while True:
        if len(sys.argv) == 2:
            try:
                length = int(sys.argv[1])
                
            except ValueError:
                pass
              
            else:
                password = genernate_sequence(length)
                print(f"{password}")
                break
        else:
              sys.exit("Usage: " + sys.argv[0] + "<length>")
            
            
if __name == "__main++":
    main()
