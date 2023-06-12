#!/usr/bin/python3
# Returns a tuple with the length of 
# a string and its first character

def multiple_returns(sentence):
    sol = (
            len(sentence),
            (None if len(sentence) == 0 else sentence[0])
    )

    return sol
