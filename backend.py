from qiskit_aer import AerSimulator
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2
from qiskit_ibm_runtime.exceptions import RuntimeJobTimeoutError
from math import log, ceil

def simulate(qc):
    job = AerSimulator().run(qc) #a AerJob object

    return getsimresult(job)


def getsimresult(job):
        result = job.result(5) #a Result object
        results = result.results #a list of ExperimentResults
        myresult = results[0] #Just one ExperimentResult
        data = myresult.data #an ExperimentResultData 
        counts = data.counts #A dictionary, string:int - string is output state, int is number of times that returned
        return counts



def saveid(job):
     id = job.job_id()
     file = open('LastJobId.txt','w+')
     file.write(id)
     file.close()


def quantumcompute(qc, backendname="ibm_brisbane"):
    #Set up service and backend (This part only needs to be run once if doing multiple runs)
    service = QiskitRuntimeService()
    backend = service.backend(backendname)

    #Compile your circuit - can dramatically increase gate counts
    pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
    compiled = pm.run(qc)
    print(compiled.draw())

    #Actually run the circuit, use Sampler to get the measurement results
    sampler = SamplerV2(backend)
    job = sampler.run([compiled])
    
    #Okay, you should be able to figure this out
    print("Your job has been submitted to the cloud")
    print("Find id on the ibm website, job id",job.job_id())
    saveid(job)
    print("Then, plug it into the seejobresults(id) function")
    print("This is automated by running viewjobresults.py")








def seejobresults(id):
    service = QiskitRuntimeService()
    job = service.job(id)
    try:
        result = job.result(5)
    except RuntimeJobTimeoutError:
         print("Results not ready yet")
         return
    data = result[0].data.c
    counts = data.get_counts()
    return counts





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