from qiskit import QuantumCircuit, ClassicalRegister
from backend import simulate, seejobresults, printcounts, quantumcompute 


qc = QuantumCircuit(123,123)
qc.h(0)
for i in range(3):
     qc.cx(i,i+1)

qc.h(0)
qc.h(2)
qc.h(3)
for i in range(4):
    qc.measure(i,i)

print(qc.draw())

printcounts(simulate(qc))
print()
printcounts(seejobresults('czebxqyhfwp00088kmk0'))

inp =  input("Run on a Real Quantum Computer? (yes to continue) ")
if 'y' in inp and 'cd' not in inp and len(inp) <= 5 and len(inp) > 1:
    print("Okay, running. ")
    quantumcompute(qc)
