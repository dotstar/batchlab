from numpy import random
from time import time
import os


# Initialize parameters from environment, or use defaults.
loops = int(os.environ.get('LOOPS',10))
matrix_size=int(os.environ.get('MATRIX_SIZE',2048))
seed=int(os.environ.get('SEED',2020))


if __name__ == "__main__":
    x = y = matrix_size
    random.seed(seed)

    starttime = time()
    for i in range(loops):
        m1 = random.rand(x,y)
        m2 = random.rand(x,y)
        m3 = m1 * m2
    stoptime = time()
    runtime = stoptime - starttime
    results = f'calculated {loops} loops of {matrix_size}x{matrix_size} matrix multiplies in {runtime} seconds'
    print(results)
