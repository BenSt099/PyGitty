import argparse
import os
import json
from FileSystemScanner import getAllFilesInFolder

def printVersion():
    print("PyGitty - V1.0.0")

def checkStatus():
    print("PiGitty - Status")

def initRepo():
    writeToJSONConfigFile(os.getcwd())
    
def writeToJSONConfigFile(input):
    with open("pygittyconfig.json", "w+") as outfile:
        json.dump(input, outfile)

def inputArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--version','-version', dest='printVersion',action='store_true', help='Displays Version of PyGitty')
    parser.add_argument('--status','-status', dest='status',action='store_true', help='Displays Current Status of PyGitty')
    parser.add_argument('--add','-add', dest='add',action='store_true', help='Adds file to a commit')
    parser.add_argument('--commit','-commit', dest='commit',action='store_true', help='Finishes Commit')
    args = parser.parse_args()

    if args.printVersion:
       printVersion()
    if args.status:
       checkStatus()

def startPiGitty():
    inputArgs()

startPiGitty()