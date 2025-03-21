from backend import  seejobresults, printcounts

printcounts(seejobresults(open('LastJobId.txt').read()))
