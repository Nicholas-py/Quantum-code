from qiskit_aer import AerSimulator
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2
from qiskit_ibm_runtime.exceptions import RuntimeJobTimeoutError
from math import log, ceil
from qiskit import QuantumCircuit

service = QiskitRuntimeService()



def simulate(qc):
    job = AerSimulator().run(qc) #a AerJob object

    return getsimresult(job)


def getsimresult(job):
        result = job.result(5) #a Result object
        results = result.results #a list of ExperimentResults
        myresult = results[0] #Just one ExperimentResult
        data = myresult.data #an ExperimentResultData
        try:
            counts = data.counts #A dictionary, string:int - string is output state, int is number of times that returned
        except AttributeError:
             print("No counts returned. Did you remember to measure your circuit? ")
             return
        return counts



def saveid(job):
     id = job.job_id()
     file = open('LastJobId.txt','a')
     file.write('\n'+id)
     file.close()

#Warning - can dramatically increase gate counts
def compilecircuit(qc, backendname="ibm_kyiv"):
    backend = service.backend(backendname)
    pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
    compiled = pm.run(qc)
    return compiled


def quantumcompute(qc, backendname="ibm_kyiv"):
    backend = service.backend(backendname)

    sampler = SamplerV2(backend)
    job = sampler.run([qc])
    
    print("Your job has been submitted to the cloud")
    print("Find id on the ibm website, job id",job.job_id())
    saveid(job)
    print("Then, plug it into the seejobresults(id) function")
    print("This is automated by running viewjobresults.py")




def measureall(qc):
     qc.measure(list(range(qc.num_clbits)),list(range(qc.num_clbits)))



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