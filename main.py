from qiskit import QuantumCircuit, ClassicalRegister
from backend import simulate, seejobresults, printcounts, quantumcompute 



step=2
n = 4
qc = QuantumCircuit(step*(n+1),step*(n+1))
qc.h(0)
for i in range(0,step*n,step):
     qc.cx(i,i+step)

for i in range(step*n+1):
    qc.measure(i,i)


printcounts(simulate(qc))
