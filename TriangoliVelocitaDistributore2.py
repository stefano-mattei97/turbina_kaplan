import matplotlib.pyplot as plt
import numpy as np
import math


def TriangoliVelocitaDistributore2 (Cr1, Cut,step,chord,alphamax,Cr0):

    plt.figure()
    scala=25
    ax = plt.subplot(111)
    ax.set_aspect(1)
    chord = scala * chord
    # plot velocità

    alpha0 = math.radians(alphamax)
    Vgt = Cr0*np.tan(alpha0)
    Vgx = Cr0
    ax.arrow(Vgt, Vgx, -Vgt, -Vgx, length_includes_head=True, width=0.15, facecolor='y')
    ax.arrow(0, -chord, Cut[step], -Cr1, length_includes_head=True, width=0.15, facecolor='b')

    first_digit = 6
    second_digit = 4
    third_digit = 12



    xcoord = np.linspace(0, chord, num=200)
    yc = np.zeros(len(xcoord))
    ratioxc = xcoord / chord

    for i in range(len(yc)):
        if xcoord[i] >= 0 and xcoord[i] < second_digit * chord / 10:
            yc[i] = first_digit / 100 * xcoord[i] / (second_digit / 10) ** 2 * (2 * second_digit / 10 - ratioxc[i])
        if xcoord[i] >= second_digit * chord / 10 and xcoord[i] < chord:
            yc[i] = first_digit / 100 * (chord - xcoord[i]) / (1 - second_digit / 10) ** 2 * (
                        1 + ratioxc[i] - 2 * second_digit / 10)

    # NACA ASIMMETRICO CON INARCAMENTO

    ratiodycdx = np.zeros(len(xcoord))
    for i in range(len(yc)):
        if xcoord[i] >= 0 and xcoord[i] < second_digit * chord / 10:
            ratiodycdx[i] = (2 * first_digit / 100) / (second_digit / 10) ** 2 * (second_digit / 10 - ratioxc[i])
        if xcoord[i] >= second_digit * chord / 10 and xcoord[i] < chord:
            ratiodycdx[i] = ((2 * first_digit / 100) / (1 - second_digit / 10) ** 2) * (second_digit / 10 - ratioxc[i])

    yt = 5 * third_digit / 100 * chord * (
                0.2969 * ratioxc ** 0.5 - 0.1260 * ratioxc - 0.3516 * ratioxc ** 2 + 0.2843 * ratioxc ** 3 - 0.1015 * ratioxc ** 4)

    teta = np.arctan(ratiodycdx)

    xextra = xcoord - yt * np.sin(teta)
    xintra = xcoord + yt * np.sin(teta)
    yextra = yc + yt * np.cos(teta)
    yintra = yc - yt * np.cos(teta)


    ax.plot(-yc,-xcoord, color='k', ls='--')
    ax.plot(-yextra, -xextra, color='k')
    ax.plot(-yintra, -xintra, color='k')
    ax.set_aspect(1)
    ax.set_xlabel('y coord')
    ax.set_ylabel('x coord')
    ax.set_title('NACA' + str(first_digit) + str(second_digit) + str(third_digit))

    #plot velocità

    plt.legend(['C0','C1'], prop={'size': 6}, loc='upper right')
    plt.yticks([0,-5,-10,-15,-20,-25],[0, 5, 10, 15, 20,25])
    assex=np.linspace(-10,10,100)
    asseyingresso=np.zeros(len(assex))
    asseyuscita = np.zeros(len(assex))
    asseyuscita = asseyuscita-chord
    plt.plot(assex,asseyingresso,color='red',ls='--')
    plt.plot(assex,asseyuscita,color='red',ls='--')
    if step == 5:
        plt.title('Triangoli velocità Distributore Midspan',)
    if step == 0:
        plt.title('Andamento velocità Distributore',)
    if step == 10:
        plt.title('Triangoli velocità Distributore Tip',)



    plt.show()


    return()
