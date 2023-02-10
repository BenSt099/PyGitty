import argparse
import os
import sys
import json
from pathlib import Path
from FileSystemScanner import get_files_with_path
from colorama import init as colorama_init
from colorama import deinit
from colorama import Fore, Style

def printVersion():
    print("◯‍◯‍◯‍ PyGitty - V1.2.0")

def addToCommit(filename):
    dictTemp = {}
    print()
    files_dict = get_files_with_path(Path(os.getcwd()).parent.absolute())
    for f in files_dict:    
        if f == filename:
            dictTemp[f] = files_dict[f]
    with open("pygittytemp.json", "w+") as outfile:
        json.dump(dictTemp, outfile, indent=4)

def commitToRepo():    
    #dictInfo = {}
    #files_dict = get_files_with_path(Path(os.getcwd()).parent.absolute()) # all files in repository: key (filename), value (path)
    #for f in files_dict:
    #    dictInfo[f] = os.path.getmtime(files_dict[f])
    files_dictTemp = readFromJSONTempFile()
    files_dictConfig = readFromJSONConfigFile()

    for f in files_dictConfig:
        for k in files_dictTemp:
            if f == k:
                files_dictConfig[f] = os.path.getmtime(files_dictTemp[k])

    writeToJSONConfigFile(files_dictConfig)   
    writeToJSONTempFile() 
    

def checkStatus():
    print("🔶 PiGitty - Status")
    colorama_init()
    files_dict = get_files_with_path(Path(os.getcwd()).parent.absolute()) # all files in repository
    filesStatusRed = []
    filesStatusGreen = []
    data = readFromJSONConfigFile()
    for files in files_dict:
        for d in data:
            if files == d:
                if data[d] != os.path.getmtime(files_dict[files]):
                    #print(Fore.RED + files)
                    filesStatusRed.append(files)

    temp_data = readFromJSONTempFile()
    for f in temp_data:
        for fsr in filesStatusRed:
            if f == fsr:
                filesStatusGreen.append(f)
                filesStatusRed.remove(f)

    print()
    print("Changes staged for commit:")
    for i in filesStatusGreen:
        print(Fore.GREEN + i)
    print()            
    print(Style.RESET_ALL)
    print("Changes not staged for commit:")            
    for k in filesStatusRed:
        print(Fore.RED + k)
    print(Style.RESET_ALL)
    deinit()


def initRepo():
    if os.getcwd().endswith(".pygitty"):

        path_To_JSON = os.path.join(os.getcwd(),"pygittyconfig.json")

        if not os.path.exists(path_To_JSON):
            with open(path_To_JSON, 'w') as json_file:
                json.dump({}, json_file)

        path_To_JSON = os.path.join(os.getcwd(),"pygittytemp.json")

        if not os.path.exists(path_To_JSON):
            with open(path_To_JSON, 'w') as json_file:
                json.dump({}, json_file)
    
        print("✅ Initialisation Successful")
    else:
        print("❌ Not A PyGitty Repository")

def isRepoInRightCondition():
    if os.getcwd().endswith(".pygitty"):
        return False
    return True    

def writeToJSONConfigFile(input):
    with open("pygittyconfig.json", "w+") as outfile:
        json.dump(input, outfile, indent=4)

def writeToJSONTempFile():
    with open("pygittytemp.json", "w") as outfile:
        json.dump({}, outfile)

def readFromJSONConfigFile():
    with open("pygittyconfig.json", "r") as out:
        data = json.load(out)
    return data

def readFromJSONTempFile():
    with open("pygittytemp.json", "r") as out:
        data = json.load(out)
    return data

def updateTimeStampInJSON():
    writeToJSONConfigFile("-") # FIX ME

def inputArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--version','-version', dest='printVersion',action='store_true', help='Displays Version of PyGitty')
    parser.add_argument('--status','-status', dest='status',action='store_true', help='Displays Current Status of PyGitty')
    parser.add_argument('-add', help='Adds file to a commit')
    parser.add_argument('--commit','-commit', dest='commit',action='store_true', help='Finishes Commit')
    parser.add_argument('--init','-init', dest='init',action='store_true', help='Initialises a Pygitty repository')
    args = parser.parse_args()

    if args.printVersion:
       printVersion()
    elif args.status:
       checkStatus()
    elif args.init:
       initRepo()
    elif args.add:
        addToCommit(args.add)
    elif args.commit:
        commitToRepo()
    else:
        print("PyGitty - Wrong Parameter")    

def startPyGitty():
    if isRepoInRightCondition == False:
        sys.exit("❌ Wrong Conditions in Repository")
    inputArgs()

startPyGitty()