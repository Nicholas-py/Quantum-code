from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator, AerJob
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2
from qiskit_ibm_runtime.exceptions import RuntimeJobTimeoutError
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
import matplotlib.pyplot as plt
from math import ceil, log
from backend import simulate, seejobresults, printcounts, quantumcompute 

backend = AerSimulator()

qc = QuantumCircuit(123,123)
qc.h(0)
for i in range(3):
     qc.ecr(i,i+1)

qc.h(0)
qc.h(2)
qc.h(3)
for i in range(4):
    qc.measure(i,i)

print(qc.draw())

printcounts(simulate(qc))
printcounts(seejobresults('czdm7bxr3jrg008pfbtg'))

inp =  input("Run on a Real Quantum Computer?")
if 'y' in inp and 'cd' not in inp and len(inp) <= 5:
    print("Okay, running. ")
    service = QiskitRuntimeService()
    kyiv = service.backend("ibm_kyiv")
    quantumcompute(qc,kyiv)