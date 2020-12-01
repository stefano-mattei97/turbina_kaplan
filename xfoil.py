import os
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


def callXF(NACA, NNodes, Re, iter, inputFile, nacaFile, polarFile, AoAmin, AoAmax, AoAdelta):
    if os.path.exists(inputFile):
        os.remove(inputFile)
    if os.path.exists(polarFile):
        os.remove(polarFile)
    if os.path.exists(nacaFile):
        os.remove(nacaFile)

    # Create input file
    fid = open(inputFile, "w")
    fid.write("PLOP\n")
    fid.write("G F\n\n")
    fid.write("NACA " + NACA + "\n")
    fid.write("PPAR\n")
    fid.write("N " + NNodes + "\n")
    fid.write("\n\n")
    fid.write("PSAV " + nacaFile + "\n")
    fid.write("OPER\n")
    fid.write("visc " + Re + "\n")
    fid.write("iter " + iter + "\n")
    fid.write("pacc " + "\n")
    fid.write(polarFile + "\n\n")
    fid.write("aseq " + AoAmin + " " + AoAmax + " " + AoAdelta + "\n")
    fid.write("\n")
    fid.write("quit")
    fid.close()

    # Run the XFoil calling command
    command = 'xfoil.exe < ' + inputFile
    os.system(command)

    df = pd.read_csv(polarFile, skiprows=11, sep="\s+")
    df.columns = ["AoA", "CL", "CD", "CDp", "CM", "Top_Xtr", "Bot_Xtr"]
    pf = polarFile + '.csv'
    df.to_csv(polarFile)
    '''
    plt.plot(df['AoA'], df['CL'])
    plt.show()
    plt.close()
    plt.plot(df['AoA'], df['CDp'])
    plt.show()
    plt.close()
    '''
    clpolar = interp1d(df['AoA'], df['CL'], kind='cubic')
    cdpolar = interp1d(df['AoA'], df['CD'], kind='cubic')

    return clpolar, cdpolar


