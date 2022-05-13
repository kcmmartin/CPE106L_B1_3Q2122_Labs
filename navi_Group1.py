"""
WEEK 3 - Ch2 Drill Exercise 
Problem 2
"""

inputFile = input("\nInput the name of the file: ")
file = open(inputFile, 'r')
LCount = 0

for line in file:
    LCount = LCount + 1
print("The number of lines in the selected text file is: ", LCount)

while True:
    lineNum = 0
    inputNum = int(input("\nPlease input text file line number. Press 0 to quit: "))
    if inputNum >=1 and inputNum <= LCount:
        file = open(inputFile, 'r')
        for lines in file:
            lineNum = lineNum + 1
            if lineNum == inputNum:
                print(lines)
    else:
        if inputNum == 0:
            print("\n\t~~~ Program has ended. Thank You! ~~~")
            break