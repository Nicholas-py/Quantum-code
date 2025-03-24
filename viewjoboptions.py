import matplotlib.pyplot as plt
from math import ceil, log

def isbinary(string):
    for i in string:
          if i not in '01':
               return False
    return True


def tobinstring(countdict):
     new = {}
     keys = list(countdict.keys())
     base = 10
     if keys[0][1] == 'x':
            base = 16
     elif isbinary(keys[0]):
          base = 2
     else:
         print("Warning: Invalid entry dictionary. Sample entry:",keys[0])
         print("Returning input unchanged")
         return countdict
     ints = list(map(lambda x:int(x,base), keys))
     binsize = ceil(log(max(ints+[1]),2))
     for i in countdict.keys():
          tobin = bin(int(i,base))
          string = tobin[2:]
          while len(string) < binsize:
               string = '0'+string
          new[string] = countdict[i]
     return new


def printcounts(counts, threshold = True):
    if not counts:
         return
    bins = tobinstring(counts)
    hasprinted = False
    for i in bins:
        if bins[i]>1 or not threshold:
            print(i," -> ",bins[i])
            hasprinted = True
    if not hasprinted:
         print("No actual results, just noise")


def listresults(lastresults):
    printcounts(lastresults)

def graphresults(lastresults):
    data = tobinstring(lastresults)
    plt.bar(list(data.keys()), list(data.values()))
    plt.xticks(rotation=-90)
    plt.show(block=False)

def qubitresults(lastresults):
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