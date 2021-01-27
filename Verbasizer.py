def lookingForFile ():
    fileWanted = False
    wantFile = input ("Do you have a previous draft that you would like to continue? [Y/N]: ")
    wantFile = wantFile.upper()
    if len(wantFile) != 0:
        if "Y" in wantFile or "YES" in wantFile:
            fileWanted = True
        elif "N" in wantFile or "NO" in wantFile:
            fileWanted = False
        else:
            while "Y" not in wantFile and "YES" not in wantFile and "N" not in wantFile and "NO" not in wantFile:
                print("Error: Please only enter Y or N.")
                wantFile = input ("[Y/N]?: ")
                wantFile = wantFile.upper()
                if "Y" in wantFile or "YES" in wantFile:
                    fileWanted = True
    else:
        while len(wantFile) == 0:
            print("Error: Please only enter Y or N.")
            wantFile = input ("[Y/N]?: ")
            wantFile = wantFile.upper()
            if len(wantFile) != 0:
                if "Y" in wantFile or "YES" in wantFile:
                    fileWanted = True
                elif "N" in wantFile or "NO" in wantFile:
                    fileWanted = False
                else:
                    while "Y" not in wantFile and "YES" not in wantFile and "N" not in wantFile and "NO" not in wantFile:
                        print("Error: Please only enter Y or N.")
                        wantFile = input ("[Y/N]?: ")
                        wantFile = wantFile.upper()
                        if "Y" in wantFile or "YES" in wantFile:
                            fileWanted = True
    return fileWanted

def promptForFile ():
    print("")
    fileName = input ("Please enter the file name of your previous draft: ")
    print("")
    if len(fileName) == 0:
        fileName = input("Please enter a file name: ")
        print("")
        while len(fileName) == 0:
            fileName = input("Please enter a file name: ")
        print("")
    return fileName

def readFile(file):
    fileObj = open(file, "r")
    lines = fileObj.read().splitlines()
    fileObj.close()
    return lines

def printList ():
    for x in list:
        print(x)

def correctDraft():
    draftWanted = False
    print("")
    response = input("Is this the correct draft? [Y/N]: ")
    response = response.upper()
    if len(response) != 0:
        if "Y" in response or "YES" in response:
            draftWanted = True
            print("")
        elif "N" in response or "NO" in response:
            draftWanted = False
        else:
            while "Y" not in response and "YES" not in response and "N" not in response and "NO" not in response:
                print("Error: Please only enter Y or N.")
                response = input ("[Y/N]?: ")
                response = response.upper()
                if "Y" in response or "YES" in response:
                    draftWanted = True
    else:
        while "Y" not in response and "YES" not in response and "N" not in response and "NO" not in response:
            print("Error: Please only enter Y or N.")
            response = input ("[Y/N]?: ")
            response = response.upper()
            if "Y" in response or "YES" in response:
                draftWanted = True
    return draftWanted

def storeWords ():
    words = []
    userWord = input("Please enter any words you would like (enter a blank to exit): ")
    words.append(userWord)
    while len(userWord) != 0:
        userWord = input()
        if len(userWord) > 0:
            words.append(userWord)
    print("Your words:" + words)
    return words

def main ():
    print("Welcome to the Verbasizer.")
    print("")
