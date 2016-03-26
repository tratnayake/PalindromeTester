"""
--  SOURCE FILE:    palindromes.py
--
--  AUTHORS:        Thilina Ratnayake @tratnayake
--
--  PROGRAM:        Provided a number, determmines if it's a palindrome and then 
--                  finds the next closest number that is a palindrome.
--
--  FUNCTIONS:      process_args()         -- Parses args and determines mode.
--                  is_even(number)        -- Checks if number is an odd or 
--                                          even number.
--                  validate(number)       -- Determine if an input only has digits in it.
--                  chunk(number)          -- Splits number into chunks.
--                  check(left,right)      -- Checks two chunks to determine if
--                                            string is a palindrome.
--                  is_palindrome(number)  -- Parent method to determine if number is a
--                                            palindrome.
--                  next_palindrome(number)-- Finds next number that's a palindome.
--                  format_output(value)   -- Converts output to "Yes" "No" per spec.
--
--  DATE:           March 16, 2016
--

--  NOTES: Coding challenge for X
--
--
--  USAGE:
--  python palindromes.py
--
--  TESTING:
--   Tests will automatically be run on start-up.
"""
import sys
import unittest

#Break this up into a seperate function so that it can be added to if requirements
#change.
def validate(input):
    """
    " Check that the user has only entered text.
    """
    return str(input).isdigit()

def process_args():
    """
    " On program start, process arguments. Determine if user expects prompts
    or has supplied command line arguments.
    """
    # If user entered no arguments, assume its a command line application.
    if(len(sys.argv) <= 1):
        input = raw_input("Please enter a number to check: ")

    elif(len(sys.argv) > 1):
       input = sys.argv[1];

    if(validate(input)):
        return int(input)
    else:
        print "Please ensure your input only contains numbers"
        sys.exit(0)



def is_even(number):
    """
    Check if the provided number is even.
    """
    if (number % 2 == 0):
        return True
    else:
        return False

def chunk(number):
    """
    Split a given number into equal chunks. If the number is not even, omit the 
    middle number.
    """
    length = len(str(number))
    if(is_even(length)):
        #If the length is even. Find the mid point.
        midpoint = length / 2;
        #print "Midpoint is ", midpoint
        #Everything up until midpoint, put in one collection
        left = str(number)[:midpoint]
        right = str(number)[midpoint:length]

    elif(not is_even(length)):
        midpoint = abs(length / 2) + 1
        #print "Midpoint is ", midpoint

        left = str(number)[:midpoint - 1]
        right = str(number)[midpoint:length]

    return {'left': left, 'right': right}


def check(left,right):
    """
    Check if two chunks of characters match each other according to their position in
    reverse.
    """
    for x in xrange(0,len(left)):
        #Check that position 0 of Chunk 1 (1) matches 
        #corresponding position from the end in Chunk 2
        if(not left[x] == right[(len(right))- x -1]):
            #If there are any that don't match, default fail.
            return False
        pass

    #If no failures (which means that the numbers match,return True)
    return True
    
def is_palindrome(number):
    """
    "Main" method to detect if a number is a palindrome.
    """
    #i.e. 1001
    #Get the length of the number
    length = len(str(number));
    #print "Length is ", length

    #If the length is 1, it is too short to be a palindrome.
    if(length <= 1):
        return False;
    #If the length is exactly 2, check if they are both the same.
    elif(length == 2):
        if str(number)[0] == str(number)[1]:
            return True;
        else:
            return False;
    #If the length is greater 2
    elif (length > 2):
        chunks = chunk(number);
        left = chunks['left']
        right = chunks['right']

        value = check(left,right)
        return value

def next_palindrome(number):
    """
    " Iterate in ascending order and check every number to determine if it is 
    a palindrome. If it is, return the number.
    """
    while True:
        number += 1
        value = is_palindrome(number)
        if(value):
            #If number is a palindrome. Break out of the loop.
            return number
        pass;



def format_output(value):
    """
    " Convert boolean response to "YES/NO" as indicated in spec.
    """
    if(value):
        print "Yes"
    else: 
        print "No"




if __name__ == '__main__':
    #Obtain the number from inputs.
    number = process_args();
    #Run number through main is_palindrome function to determine if it's a palindrome.
    value = is_palindrome(number)
    #Format the output before to convert from T/F to Y/N 
    format_output(value)
    print "Next Palindrome: ", next_palindrome(number)




