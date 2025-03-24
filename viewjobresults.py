from backend import  seejobresults
from viewjoboptions import wordstofuncs


def getresults(string):
    return seejobresults(getid(string))

def getid(string):
    if len(string) > 10:
        return string
    elif string.isdigit():
        return open('LastJobId.txt').read().split('\n')[-int(string)]
    else:
        return

def interface(lastresults):
    inp = input("Choose visualization: List, Graph, Qubit: ").lower().strip()

    if inp == '':
        print('Invalid command')
    elif inp in wordstofuncs:
        wordstofuncs[inp](lastresults)
    else:
        valid = False
        for i in wordstofuncs.keys():
            if i[0] == inp[0]:
                valid = True
                wordstofuncs[i](lastresults)
        if not valid:
            print("Invalid command")

print('Loading most recent job...')
try:
    lastresults = getresults('1')
except KeyError:
    lastresults = seejobresults(input("Enter an id: "))


interface(lastresults) 

while True:
    interface(getresults(input("Enter a # of jobs ago or id for a job: ")))