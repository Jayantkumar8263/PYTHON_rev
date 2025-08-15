'''Write a Python function that checks whether a passed string is a palindrome or not.
Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.'''

def palindrome(S):
    LSL = 0
    RSL = len(S)-1
    while RSL >= RSL :
        if RSL == LSL:
            return True
        
        RSL += 1
        LSL += 1
    return(True)
print(palindrome('mam'))