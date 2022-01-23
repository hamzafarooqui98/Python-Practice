

def palindromeCheck(palindromList):
    reversedList = palindromList[::-1]
    if reversedList == palindromList:
        return True
    else:
        return False


def checkForAlphaNumeric(text):
    alphaNumericCheck = text.isalnum()
    return alphaNumericCheck


def main():
    text = input("Enter string to test for palindrome or type 'exit' to end: ")
    palindromeList = []
    while(text != "exit"):

        if checkForAlphaNumeric(text):
            textInList = list(text.upper())
            print("Palindrom test:", palindromeCheck(textInList))

        else:
            textInList = list(text.upper())

            for value in textInList:
                if (ord(value) >= 48 and ord(value) <= 57) or (ord(value) >= 65 and ord(value) <= 90) or (ord(value) >= 97 and ord(value) <= 122):
                    palindromeList.append(value)

            print("Palindrom test:", palindromeCheck(palindromeList))
        text = input(
            "Enter string to test for palindrome or type 'exit' to end: ")


if __name__ == "__main__":
    main()
