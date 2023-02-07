import argparse
import os
import sys
import json
from pathlib import Path
from FileSystemScanner import get_files_with_path

def printVersion():
    print("PyGitty - V1.0.0")

def addToCommit():
    print()

def commitToRepo():    
    print()

def checkStatus():
    print("PiGitty - Status")
   
    files_dict = get_files_with_path(Path(os.getcwd()).parent.absolute())
    #print(files_dict)
    for files in files_dict:
        os.path.getmtime(files_dict[files])

    #if not os.path.exists(os.path.join(os.getcwd(),"pygittyconfig")):
    #    print("The following files were modified")




def initRepo():
    if os.getcwd().endswith(".pygitty"):

        path_To_JSON = os.path.join(os.getcwd(),"pygittyconfig.json")

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
        json.dump(input, outfile)

def updateTimeStampInJSON():
    writeToJSONConfigFile("-") # FIX ME


def inputArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--version','-version', dest='printVersion',action='store_true', help='Displays Version of PyGitty')
    parser.add_argument('--status','-status', dest='status',action='store_true', help='Displays Current Status of PyGitty')
    parser.add_argument('--add','-add', dest='add',action='store_true', help='Adds file to a commit')
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
        addToCommit()
    elif args.commit:
        commitToRepo()
    else:
        print("PyGitty - Wrong Parameter")    

def startPyGitty():
    if isRepoInRightCondition == False:
        sys.exit("❌ Wrong Conditions in Repository")
    inputArgs()

startPyGitty()