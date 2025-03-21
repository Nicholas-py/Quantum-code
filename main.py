from qiskit import QuantumCircuit, ClassicalRegister
from backend import simulate, seejobresults, printcounts, quantumcompute 


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
    quantumcompute(qc)
