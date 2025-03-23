from cProfile import label
from os import times
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
from matplotlib.animation import FuncAnimation, PillowWriter

df = pd.read_csv(r'C:\Users\benti\Documents\PHYS 389\100ProtonConstantKineticEnergyT1.csv')
df2=pd.read_csv(r'C:\Users\benti\Documents\PHYS 389\100ProtonConstantPositionsT1.csv')
df3=pd.read_csv(r'C:\Users\benti\Documents\PHYS 389\100ProtonConstantTimesT1.csv')
df4 = pd.read_csv(r'C:\Users\benti\Documents\PHYS 389\100ProtonConstantKineticEnergyT2.csv')
df5=pd.read_csv(r'C:\Users\benti\Documents\PHYS 389\100ProtonConstantPositionsT2.csv')
df6=pd.read_csv(r'C:\Users\benti\Documents\PHYS 389\100ProtonConstantTimesT2.csv')
df7 = pd.read_csv(r'C:\Users\benti\Documents\PHYS 389\100ProtonConstantKineticEnergyT3.csv')
df8=pd.read_csv(r'C:\Users\benti\Documents\PHYS 389\100ProtonConstantPositionsT3.csv')
df9=pd.read_csv(r'C:\Users\benti\Documents\PHYS 389\100ProtonConstantTimesT3.csv')

data = pd.DataFrame(df).to_numpy()
data2 = pd.DataFrame(df2).to_numpy()
data3 = pd.DataFrame(df3).to_numpy()
data4 = pd.DataFrame(df4).to_numpy()
data5 = pd.DataFrame(df5).to_numpy()
data6 = pd.DataFrame(df6).to_numpy()
data7 = pd.DataFrame(df7).to_numpy()
data8 = pd.DataFrame(df8).to_numpy()
data9 = pd.DataFrame(df9).to_numpy()
Positions=data2[:,1:]
Bunch_Kinetic_Energies=data[:,1]
Times=data3[:,1]
Bunch_Kinetic_Energies2=data4[:,1]
Positions2=data5[:,1:]
Times2=data6[:,1]
Bunch_Kinetic_Energies3=data7[:,1]
Positions3=data8[:,1:]
Times3=data9[:,1]
X_1=Positions[:,0]
Y_1=Positions[:,1]
Z_1=Positions[:,2]
X_2=Positions2[:,0]
Y_2=Positions2[:,1]
Z_2=Positions2[:,2]
X_3=Positions3[:,0]
Y_3=Positions3[:,1]
Z_3=Positions3[:,2]
plt.plot(Times,X_1,"-b", label="Timestep 1")
plt.plot(Times2,X_2,"-r", label="Timestep 2")
plt.plot(Times3,X_3,"-y", label="Timestep 3")
sample_rate = 1000000
start_time = 0
end_time = 1
time = np.arange(start_time, end_time, 1/sample_rate)
frequency = 1
amplitude = 1.075
theta = 0
sinewave = amplitude * np.sin(2 * np.pi * frequency * time + theta)
plt.plot(6.55945*time/1e3,sinewave,"-g", label="Truth")
plt.legend(loc="upper right")
plt.xlabel('times(s)')
plt.ylabel('x-position(m)')
plt.title('Trajectory(x) of the Proton as a Function of Time(t) for different timesteps')
plt.show()
plt.plot(Times,Bunch_Kinetic_Energies/1.6E-19,"-b", label="Timestep 1")
plt.plot(Times2,Bunch_Kinetic_Energies2/1.6E-19,"-r", label="Timestep 2")
plt.plot(Times3,Bunch_Kinetic_Energies3/1.6E-19,"-y", label="Timestep 3")
plt.axhline(y=8.9250561917715e-22/1.6E-19,color='green',label="Truth")
plt.legend(loc="upper left")
plt.xlabel('times(s)')
plt.xlim(0,0.007)
plt.ylabel('Kinetic Energy(eV)')
plt.title('Kinetic Energy(E) of the Proton as a Function of Time(t) for different timesteps')

plt.show()
plt.plot(X_3,Y_3)
plt.show()
print(100*(np.sqrt(Bunch_Kinetic_Energies3[-1])-np.sqrt(Bunch_Kinetic_Energies3[0]))/np.sqrt(Bunch_Kinetic_Energies3[0]))