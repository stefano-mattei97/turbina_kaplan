import matplotlib.pyplot as plt
import numpy as np


def TriangoliVelocitaDistributore (Cr1, Vgv, Cut,step):
    plt.figure()
    ax = plt.subplot(111)
    ax.set_aspect(1)
    ax.arrow(0, 0,0, -Vgv, length_includes_head=True, width=0.15, facecolor='y')
    ax.arrow(0, -Vgv, Cut[step],-Cr1, length_includes_head=True, width=0.15, facecolor='b')
    plt.legend(['C0','C1'], prop={'size': 6}, loc='upper right')
    if step == 5:
        plt.title('Triangoli velocità Distributore Midspan',)
    if step == 0:
        plt.title('Triangoli velocità Distributore Hub',)
    if step == 10:
        plt.title('Triangoli velocità Distributore Tip',)



    plt.show()


    return()


