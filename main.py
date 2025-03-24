from qiskit import QuantumCircuit, ClassicalRegister
from backend import simulate, measureall
from viewjoboptions import printcounts
from math import tau



qc = QuantumCircuit(3,3)
qc.x(0)
qc.h(1)
qc.ry(-tau/8,2)
qc.cz(2,1)
qc.ry(tau/8,2)
qc.z(1)
qc.sdg(2)
qc.ecr(1,2)
measureall(qc)

if __name__ == '__main__':
    print(qc.draw())
    printcounts(simulate(qc))
