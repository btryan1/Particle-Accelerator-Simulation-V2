from os import times
from turtle import color
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
from matplotlib.animation import FuncAnimation, PillowWriter

df = pd.read_csv(r'C:\Users\benti\Documents\PHYS 389\100ProtonPositions2.csv')
df2=pd.read_csv(r'C:\Users\benti\Documents\PHYS 389\100ProtonKineticEnergy2.csv')
df3=pd.read_csv(r'C:\Users\benti\Documents\PHYS 389\100ProtonTimes2.csv')
df4=pd.read_csv(r'C:\Users\benti\Documents\PHYS 389\100ProtonSpreadI2.csv')
df5=pd.read_csv(r'C:\Users\benti\Documents\PHYS 389\100ProtonSpreadF2.csv')
df6=pd.read_csv(r'C:\Users\benti\Documents\PHYS 389\100ProtonPosSpreadI2.csv')
df7=pd.read_csv(r'C:\Users\benti\Documents\PHYS 389\100ProtonPosSpreadF2.csv')


n = 1000
number_of_frames = 1000
data = pd.DataFrame(df).to_numpy()
data2 = pd.DataFrame(df2).to_numpy()
data3 = pd.DataFrame(df3).to_numpy()
data4 = pd.DataFrame(df4).to_numpy()
data5 = pd.DataFrame(df5).to_numpy()
data6 = pd.DataFrame(df6).to_numpy()
data7 = pd.DataFrame(df7).to_numpy()
data8 = pd.DataFrame(df7).to_numpy()
Positions=data[:,1:]
Bunch_Kinetic_Energies=data2[:,1]
Times=data3[:,1]
T_i=data4[:,1]
T_f=data5[:,1]
PositionsI=data6[:,1:]
PositionsF=data7[:,1:]
PositionsM=data8[:,1:]
X_1=Positions[:,0]
Y_1=Positions[:,1]
Z_1=Positions[:,2]

X_I=PositionsI[:,0]
Y_I=PositionsI[:,1]
X_f=PositionsF[:,0]
Y_f=PositionsF[:,1]
X_M=PositionsM[:,0]
Y_M=PositionsM[:,1]
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
MinXI=min(X_I)
MaxXI=max(X_I)
MinYI=min(Y_I)
MaxYI=max(Y_I)
MinXF=min(X_f)
MaxXF=max(X_f)
MinYF=min(Y_f)
MaxYF=max(Y_f)
X_spreadI=MaxXI-MinXI
Y_spreadI=MaxYI-MinYI
X_spreadF=MaxXF-MinXF
Y_spreadF=MaxYF-MinYF
print(X_spreadI,X_spreadF)
print(Y_spreadI,Y_spreadF)
Times=np.insert(Times,0,0)
Times=np.delete(Times,[0,-1,-2])


plt.plot(Times,Bunch_Kinetic_Energies/1.6e-19)
plt.xlabel('times(s)')
plt.ylabel('Kinetic Energy(eV)')
plt.title('Kinetic Energy(E) of the Proton Bunch as a function of time using square RF Signal')
plt.show()
plt.scatter(X_I,Y_I,color='green')
plt.xlabel('x-position (m)')
plt.ylabel('y-position (m)')
plt.title('Our Initial Bunch Positional spread')
plt.show()
plt.plot(X_1,Y_1,color='purple')
plt.xlabel('x-position (m)')
plt.ylabel('y-position (m)')
plt.title('The Trajectory of our Proton Bunch after 7 Orbits')
plt.show()

plt.scatter(X_f,Y_f,color='red')
plt.xlabel('x-position (m)')
plt.ylabel('y-position (m)')
plt.title('Our Final Bunch Positional spread after 7 orbits')
plt.show()
plt.hist(T_i/1.6E-19,color='green')
plt.xlabel('Kinetic energy (eV)')
plt.ylabel('Frequency')
plt.title('Our Initial Kinetic Energy Spread for our Bunch')
plt.show()
plt.hist(T_f/1.6E-19,color='red')
plt.xlabel('Kinetic energy (eV)')
plt.ylabel('Frequency')
plt.title('Our Final Kinetic Energy Spread for our Bunch')
plt.show()
Miny=min(Y_1)
Min=min(Y_1)
print((Bunch_Kinetic_Energies[-1]-Bunch_Kinetic_Energies[0])/1.6e-19)