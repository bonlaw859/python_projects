
# This program uses a constant variable CON to draw a saguaro cactus of varying sizes.

CON = 3
end = CON*2
my_range = range(1,end)

# define the main function, that runs functions that print top, middle,
# and bottom sections of the cactus

def main():
    top()
    mid()
    bot()

# top function prints the top third of the cactus, with the first unique line
# and then a for loop for the subsequent lines.

def top():
    print(' '+'x'*CON+' '*(CON+1)+'xx'*CON)
    for loop in my_range:
        print('X'+'-'*CON+'X'+' '*(CON-1)+'X'+'/' * loop+'-' * (CON*2 - loop)+'X')

# mid function prints the middle third of the cactus, with the first unique line
# and then a for loop for the subsequent lines.

def mid():
    print(' '+'xx'*CON+'X'+'~~'*CON+'X'+' '*CON+'x'*CON)
    for loop in my_range:
        print('  '*CON+' X'+'-'*loop+'\\'*(CON*2-loop)+'X'+' '*(CON-1)+'X'+'-'*CON+'X')

# bot function prints the bottom third of the cactus, with the first unique line
# and then a for loop for the subsequent lines.

def bot():
    print(' '*(CON*2+1)+'X'+'~~'*CON+'X'+'x'*(CON*2))
    for loop in my_range:
        print(' '*(CON*2+1)+'X'+'~~'*CON+'X')

# call main

main()
