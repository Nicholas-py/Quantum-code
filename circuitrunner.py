from backend import quantumcompute, compilecircuit
from main import qc

compiled = compilecircuit(qc)
print(compiled.draw())

inp =  input("Confirm run on a Real Quantum Computer? (yes to continue) ")
if 'y' in inp and 'cd' not in inp and len(inp) <= 5 and len(inp) > 1:
    print("Okay, running. ")
    quantumcompute(compiled)
else:
    print("Okay, will not run.")
