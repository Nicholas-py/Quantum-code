from backend import  seejobresults, printcounts, tobinstring
import matplotlib.pyplot as plt

print('Loading...')
id = open('LastJobId.txt').read().split('\n')[-1]
lastresults = seejobresults(id)

def listresults():
    printcounts(lastresults)

def graphresults():
    data = tobinstring(lastresults)
    plt.bar(list(data.keys()), list(data.values()))
    plt.xticks(rotation=-90)
    plt.show(block=False)
    input()

def qubitresults():
    data = tobinstring(lastresults)
    keys = list(data.keys())
    l = len(keys[0])
    total = sum(data.values())

    print("Chance of being 1: ")
    for i in range(l):
        ones = 0
        for string in keys:
            if string[-(i+1)] == '1':
                ones += data[string]
        percent = round(100*ones/total,2)
        print(f"Qubit {i}: {percent}%")

wordstofuncs = {'list':listresults, 'graph':graphresults,'qubit':qubitresults}




inp = input("Choose visualization: List, Graph, Qubit: ").lower().strip()
if inp == '':
    print('Invalid command')
elif inp in wordstofuncs:
    wordstofuncs[inp]()
else:
    valid = False
    for i in wordstofuncs.keys():
        if i[0] == inp[0]:
            valid = True
            wordstofuncs[i]()
    if not valid:
        print("Invalid command")

