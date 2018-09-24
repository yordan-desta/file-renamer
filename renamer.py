import os
import commonLib

def renameFile(oldName, newName):
    if not commonLib.isFile(oldName):
        return False

    if (os.path.isfile(oldName)):
        os.rename(oldName, newName)

        return True

    return False


def appendNameOnFilesInDir(path, appendName):
    if (os.path.isdir(path)):

        for eachFile in os.listdir(path):

            if str.endswith(eachFile, "/"):
                appendNameOnFile(path + eachFile, appendName)
            else:
                appendNameOnFile(path + "/" + eachFile, appendName)

        return True

    return False


def appendNameOnFile(oldPath, appendName):
    if not commonLib.isFile(oldPath):
        return False

    baseName = os.path.basename(oldPath);

    extentionArray = baseName.split(".")

    pathToFile = oldPath.split(baseName)[0]

    if len(extentionArray) > 1:

        extention = extentionArray[len(extentionArray) - 1]

        oldFileName = baseName.split("." + extention)[0]

        return renameFile(oldPath, pathToFile + oldFileName + appendName + "." + extention)

    else:

        renameFile(oldPath, pathToFile + baseName + appendName)