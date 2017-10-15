"""

This is a code written in Python 3 by Mostafa Ahangarha
as the second homework for StartingUp2017 project.

"""
import re


code = ""   # container for BrainFuck code

cell = {}   # Cells as ASCII code container

pointer = 0 # Pointer to determine which cell is under operation

outputString = "" # Container or the output of the program

# Reading code from the code file
with open("./ahangarha-code.bf", "r") as codeFile:
    for l in codeFile:
        code = code + l

# removing all non-BF characters, leaving only +-><[].
code = re.sub('[^\+-\.\[\]<>]', '', code)


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
    global cell, pointer, outputString
    
    if cell.get(pointer) is None:
        cell[pointer] = 0
    
    #print(chr(cell[pointer]))
    outputString += chr(cell[pointer])


# opening loop ([)
def open_loop():
    global cell, pointer, i
    
    if cell[pointer]==0:
        
        while code[i]!="]":
            i += 1
            
        

# closing loop (])
def close_loop():
    global cell, pointer, i
    
    if cell[pointer]!=0:
        
        while code[i]!="[":
            i -= 1
    
# =================================
# Running the BF code

# i as counter
i = 0

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

print(outputString)