import os

dictFiles = {}

def getAllFilesInFolder(folderName):
    
    analyseFolders(folderName)
    return dictFiles
    
def analyseFolders(folderName):
    for entry in os.scandir(folderName):
        if entry.is_file():
            dictFiles[entry.name] = entry.path
            yield entry.name
        elif entry.is_dir() and entry.name != ".git":
            yield from getAllFilesInFolder(entry.path)