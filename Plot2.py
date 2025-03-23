from os import times
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
from matplotlib.animation import FuncAnimation, PillowWriter

df = pd.read_csv(r'C:\Users\benti\Documents\PHYS 389\1ProtonPositionsT1.csv')
df2=pd.read_csv(r'C:\Users\benti\Documents\PHYS 389\1ProtonKineticEnergyT1.csv')
df3=pd.read_csv(r'C:\Users\benti\Documents\PHYS 389\1ProtonTimesT1.csv')
df4 = pd.read_csv(r'C:\Users\benti\Documents\PHYS 389\1ProtonKineticEnergyT2.csv')
df5=pd.read_csv(r'C:\Users\benti\Documents\PHYS 389\1ProtonPositionsT2.csv')
df6=pd.read_csv(r'C:\Users\benti\Documents\PHYS 389\1ProtonTimesT2.csv')
df7 = pd.read_csv(r'C:\Users\benti\Documents\PHYS 389\1ProtonKineticEnergyT3.csv')
df8=pd.read_csv(r'C:\Users\benti\Documents\PHYS 389\1ProtonPositionsT3.csv')
df9=pd.read_csv(r'C:\Users\benti\Documents\PHYS 389\1ProtonTimesT3.csv')


n = 1000
number_of_frames = 1000
data = pd.DataFrame(df).to_numpy()
data2 = pd.DataFrame(df2).to_numpy()
data3 = pd.DataFrame(df3).to_numpy()
data4 = pd.DataFrame(df4).to_numpy()
data5 = pd.DataFrame(df5).to_numpy()
data6 = pd.DataFrame(df6).to_numpy()
data7 = pd.DataFrame(df7).to_numpy()
data8 = pd.DataFrame(df8).to_numpy()
data9 = pd.DataFrame(df9).to_numpy()
Positions=data[:,1:]
Bunch_Kinetic_Energies=data2[:,1]
Times=data3[:,1]
Bunch_Kinetic_Energies2=data4[:,1]
Positions2=data5[:,1:]
Times2=data6[:,1]
Bunch_Kinetic_Energies3=data7[:,1]
Positions3=data8[:,1:]
Times3=data9[:,1]

def update_hist(num, data):
    print(num)
    plt.cla()
    plt.hist(data[num])

    fig = plt.figure()
    hist = plt.hist(data[7])

    animation = animation.FuncAnimation(fig, update_hist, number_of_frames, fargs=(data, ) )
        
def Extract(X_1,Y_1,Z_1):
    X=[]
    Y=[]
    Z=[]
    for i in range(0,45916,1):
        X.append(X_1[i])
        Y.append(Y_1[i])
        Z.append(Z_1[i])
    return X,Y,Z


time_percent=3.049968E-4    

X_line=[]
Y_line=[]
Z_line=[]


def update(i):
    ax.cla()

    x = X[i]
    y = Y[i]
    z = Z[i]
    X_line.append(x)
    Y_line.append(y)
    Z_line.append(z)


    ax.scatter(x, y, z, s = 10, marker = 'o')
    ax.plot(X_line, Y_line, Z_line)



    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_zlim(-0.1, 0.1)

    fig = plt.figure(dpi=150)
    ax = fig.add_subplot(projection='3d')

    anim = FuncAnimation(fig = fig, func = update, frames = frames, interval = 1, repeat = False)
    f = r'C:\Users\benti\Documents\PHYS 389\100Proton.gif'
    writergif = animation.PillowWriter(fps=30) 
    anim.save(f, writer=writergif)
    plt.show()
    plt.plot(X_1,Y_1)
    plt.axvline(x=0, c='green', lw=1, linestyle='dashed')
    plt.axvline(x=0.08, c='green', lw=1, linestyle='dashed')
    plt.axvline(x=0.4583593813062775, c='red', lw=1, linestyle='dashed')
    plt.axvline(x=0.5383593813062775, c='red', lw=1, linestyle='dashed')
    plt.axvline(x= 1.083322333768204, c='blue', lw=1, linestyle='dashed')
    plt.axvline(x= 1.1633223337682042, c='blue', lw=1, linestyle='dashed')
    plt.axvline(x= 1.8355090754786647, c='yellow', lw=1, linestyle='dashed')
    plt.axvline(x=1.9155090754786648, c='yellow', lw=1, linestyle='dashed')
    plt.axvline(x=2.692718394317757, c='purple', lw=1, linestyle='dashed')
    plt.axvline(x=2.772718394317757, c='purple', lw=1, linestyle='dashed')
    plt.axvline(x=3.644079576224505, c='grey', lw=1, linestyle='dashed')
    plt.axvline(x=3.724079576224505, c='grey', lw=1, linestyle='dashed')
    plt.axvline(x=4.6648448213261124, c='black', lw=1, linestyle='dashed')
    plt.axvline(x=4.7448448213261125, c='black', lw=1, linestyle='dashed')
    plt.show()
    Times=np.delete(Times,[0,-1,-2])
    plt.plot(Times,Bunch_Kinetic_Energies/1.6e-19)
    plt.show()
    plt.scatter(X_f,Y_f)
    plt.show()
    plt.scatter(X_1,Y_1)


    plt.show()
    plt.scatter(X_f,Y_f)
    plt.show()

Times=np.delete(Times,[0,-1])
Times3=np.delete(Times3,[0,-1])
Times2=np.delete(Times2,[0,-1])
plt.plot(Times,Bunch_Kinetic_Energies/1.6e-19,"-b", label="Timestep 1")
plt.plot(Times2,Bunch_Kinetic_Energies2/1.6e-19,"-r", label="Timestep 2")
plt.plot(Times3,Bunch_Kinetic_Energies3/1.6e-19,"-y", label="Timestep 3")
plt.legend(loc="upper left")
plt.xlabel('times(s)')
plt.ylabel('Kinetic Energy(eV)')
plt.title('Kinetic Energy(E) of the Proton as a Function of Time(t) for different timesteps over one full orbit')

plt.show()

print(((Bunch_Kinetic_Energies3[-1]-Bunch_Kinetic_Energies2[0])/1.6e-19))


