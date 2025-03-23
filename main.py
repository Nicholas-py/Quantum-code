from qiskit import QuantumCircuit, ClassicalRegister
from backend import simulate, printcounts, measureall
from math import tau



qc = QuantumCircuit(3,3)
qc.x(0)
qc.h(2)
qc.ry(-tau/8,1)
qc.cz(2,1)
qc.ry(tau/8,1)
qc.z(2)
qc.sdg(1)
qc.ecr(2,1)

measureall(qc)
printcounts(simulate(qc))
