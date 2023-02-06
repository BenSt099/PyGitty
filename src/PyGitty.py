import argparse

def printVersion():
    print("PyGitty - V1.0.0")

def checkStatus():
    print("PiGitty - Status")

def inputArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--version','-version', dest='printVersion',action='store_true', help='Displays Version of PyGitty')
    parser.add_argument('--status','-status', dest='status',action='store_true', help='Displays Current Status of PyGitty')
    args = parser.parse_args()

    if args.printVersion:
       printVersion()
    if args.status:
       checkStatus()




def startPiGitty():
    inputArgs()

startPiGitty()