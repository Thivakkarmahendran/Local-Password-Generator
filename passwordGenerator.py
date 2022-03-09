import random
import string
import sys

import pyperclip as clipboard



letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
symbols = ["!", "@", "#", "&","-"]

chances = ["smallLetter", "bigLetter", "symbol", "number"]
weights=[0.50, 0.25, 0.125, 0.125]


def generateRandomPassword(length:int = 12):
    password = ""
    
    for i in range(length):
        
        letterIndex = random.randint(0, len(letters)-1)
        symbolIndex = random.randint(0, len(symbols)-1)
        number = random.randint(0, 9)

        choice = random.choices(chances, weights)[0] 
        
        if(choice == "smallLetter"):
            password += letters[letterIndex]
        elif(choice == "bigLetter"):
            password += letters[letterIndex].upper()
        elif(choice == "symbol"):
            password += symbols[symbolIndex]
        elif(choice == "number"):
            password += "{}".format(number)
    
    return password

def isValidPassword(password: string) -> bool:
    
    containsNumber = False
    containsUpperCase = False
    containsLowerCase = False
    containsSymbol = False
    
    if(len(password) < 5):
        return False #password too short
    
    for character in password:
        if character.isdigit():
            containsNumber = True
        if character.isupper():
            containsUpperCase = True
        if not character.isupper() and not character.isdigit() and character not in symbols:
            containsLowerCase = True
        if character in symbols:
            containsSymbol = True
    
    
    return containsNumber and containsUpperCase and containsLowerCase and containsSymbol

def testCases():
    assert isValidPassword("") == False, "Should be False, empty string"
    assert isValidPassword("omdw!i79e8a3") == False, "Should be False, no uppercase letter"
    assert isValidPassword("OMDW!I79E8A3") == False, "Should be False, no lowercase letter"
    assert isValidPassword("omdWi79e8a3") == False, "Should be False, no symbol"
    assert isValidPassword("omdWiea") == False, "Should be False, no number"
    assert isValidPassword("omdW!i79e8a3") == True, "Should be True, correct password"
    

def main():
    
    testCases() #Sanity Check
    
    password = ""
    passwordLength = 12

    try:
        if(len(sys.argv) >= 2):
            passwordLength = int(sys.argv[1])
    except Exception as e:
        raise Exception("Could not read the argument: {}".format(e))
    
    loopCheck = 0
    while(not isValidPassword(password)):
        
        if(loopCheck > 10):
            raise Exception("Infinite Loop")
        
        password = generateRandomPassword(passwordLength)
        loopCheck += 1
    
    print("Randomly Generated Password: {}".format(password))
    clipboard.copy(password)
    print("Copied password to clipboard")



if __name__ == '__main__':
    main()
    
