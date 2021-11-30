# Shubhayu Shreshta
# NETID:1001724804
# Due Date: 11/30/21
# Using macOS Monterey v.12.0.1 with Python v.3.9.5

# opening file input.txt as read
inputFile = open('input.txt', 'r')

# storing contents of file
fileContents = inputFile.readlines()

# variable that will store the nest depth
nestingDepth = 0

# creating a boolean to see if it a block comment or not
inBlockComment = False

# creating a boolean to see if it a block comment or not
inQuote = False

# creating a double quote count
quoteCount = 0

# creating a blockComment count
blockCount = 0

# looping through the lines of the file content
for line in fileContents:
    # adding tokenizing the line contents in a variable called characters
    characters = list(line)

    # looping through the tokenized list 
    for currChar in range(len(characters)):
        # checking for single line comments
        if(characters[currChar] == '/' and characters[currChar+1] == '/'):
            break; 
        # checking for end of multiline comment
        elif(characters[currChar] == '*' and characters[currChar+1] == '/'):
            # since we are not in a block comment we say false
            inBlockComment = False
            blockCount -= 1
        # checking for beginning of multiline comment
        elif(characters[currChar] == '/' and characters[currChar+1] == '*'):
            # since we are now in a block comment we set the bool to true
            inBlockComment = True
            blockCount += 1
        # checking for quotes
        elif(characters[currChar] == '"'):
            # if we are in quote we set it to true
            inQuote = True
            
            # if we are in quote we set the quote count up to 1
            quoteCount += 1
            
            # if the quote count is two, and we are in a quote, then that means
            # we found the end quote, and we can set the inQuote to false and reset
            # the count variable
            if (quoteCount == 2 and inQuote == True):
                inQuote = False
                quoteCount = 0
        # checking for beginning bracket
        # with conditions if we are not in a block comment or a quote and the character is a '{'
        elif(inBlockComment == False and inQuote == False and blockCount == 0 and quoteCount == 0 and characters[currChar] == '{'):
            nestingDepth += 1
        # checking for ending bracket
        # with conditions if we are not in a block comment or a quote and the character is a '}'
        elif(inBlockComment == False and inQuote == False and blockCount == 0 and quoteCount == 0 and characters[currChar] == '}'):
            nestingDepth -= 1

    # printing the nesting depth 
    # using end=" " to consume the \n
    print(nestingDepth, end=" ")
    # printing the contents of the line
    # using end=" " to consume the \n
    print(line, end = "")

# printing out an error if there are mismatched depth
if(nestingDepth != 0):
    print("ERROR: expected ‘}’ but found EOF")
elif(quoteCount != 0):
    print("ERROR: missing \"")
elif(blockCount != 0):
    print("ERROR: missing \"")

print(quoteCount)
print(blockCount)
