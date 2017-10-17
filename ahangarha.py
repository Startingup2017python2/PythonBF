# -*- coding: utf-8 -*-
"""
This is a code written in Python 3 as the second homework
for StartingUp2017 project.

@author: Mostafa Ahangarha
"""
import re

code = ''   # container for BrainFuck code
cell = {}   # Cells as ASCII code container
pointer = 0 # Pointer to determine which cell is under operation
result = '' # Container or the output of the program
i = 0       # representing the index of character in BF code 

def resetVariables():
    global code, cell, pointer, result, i
    code = ''
    cell = {}
    pointer = 0
    result = ''
    i = 0

# incriment (+)
def inc():
    global cell, pointer
    if cell.get(pointer) is None:
        cell[pointer] = 0
    
    cell[pointer] = cell[pointer] + 1

# decriment (-)
def dec():
    global cell, pointer
    
    if cell.get(pointer) is None:
        cell[pointer] = 0
    cell[pointer] = cell[pointer] - 1

# shift right (>)
def shift_right():
    global pointer
    pointer = pointer + 1

# shift right (<)
def shift_left():
    global pointer
    pointer = pointer - 1

# output (.)
def output():
    global cell, pointer, result
    if cell.get(pointer) is None:
        cell[pointer] = 0
    
    result += chr(cell[pointer])


# opening loop ([)
def open_loop():
    global cell, pointer, i, code
    
    if cell[pointer]==0:

        inloop = True
        ignore = 0

        while inloop==True:
            i += 1 # next
            
            if code[i] != ']':
                if code[i] == '[': # inner loop
                    ignore += 1
                
            elif code[i] == ']' and ignore > 0: #closing of inner loop, ignore
                ignore -= 1
                
            else:
                inloop = False

# closing loop (])
def close_loop():
    global cell, pointer, i, code
    
    if cell[pointer]!=0:

        inloop = True
        ignore = 0
        while inloop==True:
            
            i -= 1 # previous
            
            if code[i] != '[':
                
                if code[i] == ']': # inner loop
                    ignore += 1
                
            elif code[i] == '[' and ignore > 0: #opening of inner loop, ignore
                ignore -= 1

            else:
                inloop = False

def verify_loop(code):
    code = re.sub('[^[\]]', '', code)
    control = 0
    for c in code:
        if c == '[':
            control += 1
        else:
            control -= 1
        if control < 0:
            raise ValueError("ERROR: Syntax error! Recheck loops made by [ and ].")
        
    if control != 0:
        raise ValueError("ERROR: Syntax error! Recheck loops made by [ and ].")
            

# =================================
# Running the BF code
def execute(inputCode=''):
    global cell, pointer, result, i, code
    
    resetVariables()
    
    code = inputCode
    
    # Check the input not to be empty
    if (code == ''):
        raise ValueError("ERROR: Empty code!")
    
    # removing all non-BF characters, leaving only +-><[].
    code = re.sub('[^\+-\.\[\]<>]', '', code)
    
    verify_loop(code)
    
    # Check the cleaned up input not to be empty
    if (code == ''):
        raise ValueError("ERROR: No BrainFuck character is in the code!")
    
    while i < len(code):
        # map the inputs to the function blocks
        operate = {
           '+' : inc,
           '-' : dec,
           '>' : shift_right,
           '<' : shift_left,
           '.' : output,
           '[' : open_loop,
           ']' : close_loop,
        }
        
        # c as charater
        c = code[i]
        operate[c]()
        i += 1
    
    return(result)