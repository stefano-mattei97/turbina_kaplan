import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


def Drafttube(Q,H,Ns,De,rho,g):

    #COSTANTI
    data2 = pd.read_csv('diagrammadiMoody.txt', delim_whitespace=True)
    c3 = 2                                                #velocità acqua uscita dal diffusore nota per il draft-tube scelto[m/s] tra 1.5 - 2.0
    patm = 101300                                           #[Pascal]
    pv = 2985.7                                             #tensione di vapore a T=24°C dalla tabella Rogers e Mayhew [Pascal]
    data2 = pd.read_csv('diagrammadiMoody.txt', delim_whitespace=True)
    thomacr = np.interp(Ns, data2['Ns'], data2['thoma'])    #dipende dalla tabella di Moody e Zowski e dal nostro Ns espresso in [rad] (realizzare tabella)
    etaid = 0.83                                            #efficienza draf-tube
    theta = 8                                               #angolo cono formato dalle pareti



    #DIMENSIONAMENTO DIFFUSORE (tipologia PL60-55 a gomito)
    h4 = 1.17 * De                                         #dimensioni ausiliarie (guardare grafico testo Gubin 1970)
    J = 0.363 * De                                         #dimensioni ausiliarie [m], J =(h1 + h2)
    h = 2.74 * De                                          #altezza cono + gomito [m]
    h3 = h - h4 - J                                        #altezza cono all'ingresso [m]
    h5 = 1.370 * De                                        #altezza scarico [m]
    D2 = 0.973 * De                                        #diametro effettivo cono [m]
    L = 5.0 * De                                           #lunghezza condotto scarico [m]
    B5 = B6 = 2.4 * De                                     #larghezza sezione scarico [m]
    zsc = h - h5                                           #altezza della sezione di uscita girante al di sopra del pelo libero
    He = H * etaid                                         #H netto
    D3 = ((4*Q)/ (math.pi * c3))**(1/2)                    #diametro uscita diffusore
    zscmax = (((patm - pv)/(rho *g)) - (thomacr * He))     #altezza max di scarico
    NPSH = ((patm -pv)/(rho*g))-zsc                        #altezza netta di aspirazione
    thoma = NPSH/He                                        #coefficiente di thoma

    fig = plt.figure()
    ax = plt.subplot(111)
    plt.title('Diagramma di Moody Draft-Tube')
    ax.plot(data2['Ns'], data2['thoma'], color='k', ls='-')
    plt.plot(Ns, thoma, marker='o', color='red')
    plt.plot(Ns, thomacr, marker='o', color='b')
    ax.annotate('Zona Senza Cavitazione', (2, 2), color='red')
    ax.annotate('Zona con Cavitazione', (4, 0.5), color='red')
    ax.set_xlabel('Ns[rad]')
    ax.set_ylabel('thoma')
    plt.show()
    data = {'thomacr': thomacr,'thoma':thoma,'etaid': etaid,'h4': h4,'J': J,'h': h,'h3': h3,
            'h5': h5,'D2':D2,'L':L,'B5':B5,'zsc':zsc,'He':He,'D3':D3,
            'zscmax':zscmax,'NPSH':NPSH}
    Drafttubedb = pd.DataFrame(data, columns=['thomacr','thoma', 'etaid', 'h4', 'J', 'h', 'h3',
                                              'h5','D2','L','B5','zsc','He','D3','zscmax','NPSH'], index=[0])

    return(Drafttubedb)