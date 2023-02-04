#
#
#
#
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

p = 0.5 # probabilidad de perder un dato
sample_size = np.array([10, 100, 1000, 10000])
redo_experiment = 300
bias_array = []

data = np.random.normal(size= sample_size.max())

for n in sample_size:
    sample = data[:n]

    bias = np.zeros( redo_experiment )
    for i in range(redo_experiment):
        # por probabilidad no tendremos datos en ciertos lados
        lost_data = np.random.binomial(1, p, n).astype(bool)
        sample_observada = sample[~lost_data]

        # producto de no ser random sampling, no tendremos una seccion
        sample_observada = sample_observada[ sample_observada > 0]
        bias[i] = sample_observada.mean()
    bias_array.append(bias)
    


