from backend import  seejobresults, printcounts

lastresults = seejobresults(open('LastJobId.txt').read())
print('Loaded')

def listresults():
    printcounts(lastresults)

def graphresults():
    printcounts(lastresults)

wordstofuncs = {'list':listresults, 'graph':graphresults}




inp = input("Choose visualization: List, Graph: ").lower().strip()

if inp in wordstofuncs:
    wordstofuncs[inp]()
else:
    for i in wordstofuncs.keys():
        if i[0] == inp[0]:
            wordstofuncs[i]()
    

