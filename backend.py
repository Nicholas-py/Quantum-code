from qiskit_aer import AerSimulator, AerJob
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2
from math import log, ceil


def getsimresult(job):
        result = job.result(5) #a Result object
        results = result.results #a list of ExperimentResults
        myresult = results[0] #Just one ExperimentResult
        data = myresult.data #an ExperimentResultData 
        counts = data.counts #A dictionary, string:int - string is output state, int is number of times that returned
        return counts


def simulate(qc):
    job = AerSimulator().run(qc) #a AerJob object

    return getsimresult(job)


def quantumcompute(qc, backend):
    pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
    compiled = pm.run(qc)
    print(compiled.draw())
    sampler = SamplerV2(backend)
    job = sampler.run([compiled])
    
    print("Find id on the ibm website, job id",job.job_id())
    print("Then, plug it into the seejobresults(id) function")

    return


def seejobresults(id):
    service = QiskitRuntimeService()
    job = service.job(id)
    result = job.result()
    data = result[0].data.c
    counts = data.get_counts()
    return counts



def tobinstring(countdict):
     print(countdict)
     new = {}
     keys = list(countdict.keys())
     try:
         base = {'x':16,'b':2}[keys[0][1]]
     except KeyError:
         print("Warning: Invalid entry dictionary. Sample entry:",keys[0][1])
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
    bins = tobinstring(counts)
    hasprinted = False
    for i in bins:
        if bins[i]>1 or not threshold:
            print(i," -> ",bins[i])
            hasprinted = True
    if not hasprinted:
         print("No actual results, just noise")