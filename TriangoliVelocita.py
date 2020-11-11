import matplotlib.pyplot as plt



def TriangoliVelocita(dato):
    fig = plt.figure()
    ax = plt.subplot(111)
    ax.set_aspect(1)
    ax.arrow(0, 0, dato['U'], 0, length_includes_head=True, width=0.3, facecolor='y')
    ax.arrow(0, 0, dato['Cu1'], dato['Cm'], length_includes_head=True, width=0.3, facecolor='b')
    ax.arrow(dato['U'], 0, -dato['Wu1'], dato['Cm'], length_includes_head=True, width=0.3, facecolor='g')
    ax.arrow(dato['U'], 0, -dato['Wu2'], dato['Cm'], length_includes_head=True, width=0.3, facecolor='r')
    ax.arrow(0, 0, dato['Cu2'], dato['Cm'], length_includes_head=True,label='Prova', width=0.3, facecolor='c')
    plt.legend(['U','C1','W1','W2','C2'], prop={'size': 8})
    plt.title('Triangoli velocità',)
    plt.show()
    return ()