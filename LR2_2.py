"Programming Problem 2 = LR2_2"
"Edited by: Dustin Ventura"

enterfile = input("Enter the file name: ")
file = open(enterfile, 'r')
lineCounter = 0

for line in file:
    lineCounter = lineCounter + 1

print("There are", lineCounter, "lines in this file")

while True:
    lineNumber = 0

    num = int(input("Please enter a line number or press 0 to quit: "))
    if num >=1 and num <= lineCounter:
        file = open(enterfile, 'r')
        for lines in file:
            lineNumber = lineNumber + 1
            if lineNumber == num:
                print(lines)
    else:
        if num == 0:
            print("The program has ended. Thank you for using this program!")
            break