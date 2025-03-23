from Particle import Proton
from GeneralEMField2 import EMField
import pandas as pd
from GenerateParticleBunch import ChargedParticleBunch
import numpy as np

time = 0  # initial time stamp
deltat =1e-04
  # time steps used
times = []#our times array which will store our times to later be exported as .csv using pandas
particle=Proton()#initilize's our proton class instance, which contains the needed update methods and properties of the proton
BField=EMField(electric = np.array([0,0,0], dtype=float), magnetic = np.array([0,0,-1e-5], dtype=float))#initilizes our constant B-field class instace

PB=ChargedParticleBunch()#initilizes a particle bunch class instance
CM=ChargedParticleBunch(electric = np.array([0,0,0], dtype=float), magnetic = np.array([0,0,-1E-5], dtype=float))#initilizes a particle bunch class instance with the constant B field
Bunch=PB.Generate_Bunch(1)#a 1 particle bunch
Time_period=CM.Orbit_Period(Bunch)
radius=BField.Cyclotron_Radius(Bunch[0])
Average_Positons=[]
Average_Velocities=[]
Average_Kinetic_Energies=[]
while time<=Time_period:#loops until one full orbit has been acheived 
        Averages=CM.Averages(Bunch)#updates our averages
        Average_Positons.append(Averages[0])
        Average_Velocities.append(Averages[1])
        Average_Kinetic_Energies.append(Averages[2])
        Bunch=CM.Bunch_Update(Bunch,deltat,2)
        times.append(time)
        time += deltat
#exports the data as .csv's
pd.DataFrame(Average_Kinetic_Energies).to_csv(r'C:\Users\benti\Documents\PHYS 389\100ProtonConstantKineticEnergyT1.csv')
pd.DataFrame(Average_Positons).to_csv(r'C:\Users\benti\Documents\PHYS 389\100ProtonConstantPositionsT1.csv')
  

pd.DataFrame(times).to_csv(r'C:\Users\benti\Documents\PHYS 389\100ProtonConstantTimesT1.csv')
print('Information Saved')