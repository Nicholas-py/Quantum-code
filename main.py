from qiskit import QuantumCircuit, ClassicalRegister
from backend import simulate, printcounts, measureall
from math import tau



qc = QuantumCircuit(3,3)
qc.x(0)
qc.h(2)
qc.barrier(0,1,2)
qc.ry(-tau/8,1)
qc.cz(2,1)
qc.ry(tau/8,1)
qc.barrier(0,1,2)
qc.z(2)
qc.sdg(1)
qc.barrier(0,1,2)
qc.ecr(2,1)

print(qc.draw())
measureall(qc)
printcounts(simulate(qc))
