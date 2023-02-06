import os

dictFiles = {}

def getAllFilesInFolder(folderName):
    obj = os.scandir(folderName)
    for ob in obj:
        if ob.is_file:
            dictFiles[ob.name] = ob.path
    return dictFiles