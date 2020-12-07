import numpy as np
import pandas as pd



def CanaleToroidale(Di, De,Dgv, Cu1):
    A = 0.13 * De
    B = 0.2 * De
    step = 11

    R = np.linspace(Di, De, step, endpoint=True)
    Cut= np.zeros(step)
    Delta = np.zeros(step)
    for i in range (step):
        Cut[i] = Cu1[(step-1)-i] * R[(step-1)-i]/(Dgv/2)
        Delta[i] = Cut[i]-Cu1[(step-1)-i]
    data = {'R': R,
            'Cut': Cut,
            'Delta': Delta}
    CanaleToroidaledb = pd.DataFrame(data, columns=['R', 'Cut', 'Delta'])

    return(Cut,Delta,CanaleToroidaledb)


