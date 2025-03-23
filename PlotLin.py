from os import times
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
from matplotlib.animation import FuncAnimation, PillowWriter

df = pd.read_csv(r'C:\Users\benti\Documents\PHYS 389\100ProtonPositionsLin.csv')
df2=pd.read_csv(r'C:\Users\benti\Documents\PHYS 389\100ProtonKineticEnergyLin.csv')
df3=pd.read_csv(r'C:\Users\benti\Documents\PHYS 389\100ProtonTimesLin.csv')
df4=pd.read_csv(r'C:\Users\benti\Documents\PHYS 389\100ProtonSpreadILin.csv')
df5=pd.read_csv(r'C:\Users\benti\Documents\PHYS 389\100ProtonSpreadFLin.csv')
df6=pd.read_csv(r'C:\Users\benti\Documents\PHYS 389\100ProtonPosSpreadILin.csv')
df7=pd.read_csv(r'C:\Users\benti\Documents\PHYS 389\100ProtonPosSpreadFLin.csv')



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

plt.show()
plt.plot(X_1,Y_1)

plt.axvline(x=0, c='green', lw=1, linestyle='dashed')
plt.axvline(x=0.16, c='green', lw=1, linestyle='dashed')
plt.axvline(x=0.6154511478263496, c='red', lw=1, linestyle='dashed')
plt.axvline(x=0.7754511478263496, c='red', lw=1, linestyle='dashed')
plt.axvline(x= 1.3354806371051438, c='blue', lw=1, linestyle='dashed')
plt.axvline(x= 1.4954806371051437, c='blue', lw=1, linestyle='dashed')
plt.axvline(x= 2.1429918639398884, c='yellow', lw=1, linestyle='dashed')
plt.axvline(x=2.3029918639398885, c='yellow', lw=1, linestyle='dashed')
plt.axvline(x=3.0279492460692166, c='purple', lw=1, linestyle='dashed')
plt.axvline(x=3.1879492460692167, c='purple', lw=1, linestyle='dashed')
plt.axvline(x=3.982361828666161, c='grey', lw=1, linestyle='dashed')
plt.axvline(x=4.142361828666161, c='grey', lw=1, linestyle='dashed')
plt.axvline(x= 5.001339051697443, c='black', lw=1, linestyle='dashed')
plt.axvline(x=5.161339051697444, c='black', lw=1, linestyle='dashed')
plt.xlabel('x-positon (m)')
plt.ylabel('y-position (m)')
plt.title('Trajectory of the Bunch in the Linac')
plt.show()

plt.plot(Times,Bunch_Kinetic_Energies/1.6e-19)
plt.xlabel('times(s)')
plt.ylabel('Kinetic Energy(eV)')
plt.title('Kinetic Energy(E) of the Proton Bunch as a function of time for LINAC')

plt.show()


Times=np.insert(Times,0,0)
Times=np.delete(Times,[0,-1,-2])




plt.scatter(X_I,Y_I,color='green')
plt.xlabel('x-position (m)')
plt.ylabel('y-position (m)')
plt.title('Our Initial Bunch Positional spread')
plt.show()


plt.scatter(X_f,Y_f,color='red')
plt.xlabel('x-position (m)')
plt.ylabel('y-position (m)')
plt.title('Our Final Bunch Positional spread after 7 Periods of acceleration')
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
