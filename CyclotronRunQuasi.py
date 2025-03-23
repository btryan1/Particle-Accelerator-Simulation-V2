from calendar import c
from tkinter import Y
from turtle import position
from Particle import Proton
from GeneralEMField2 import EMField
import pandas as pd
from GenerateParticleBunch import ChargedParticleBunch
import numpy as np

time = 0  # initial time stamp
time2=0
deltat =1e-06  # time steps of 1ms
SQ_Val_Multiplier=deltat/1e-6
print(SQ_Val_Multiplier)
deltat_2=0.0002E-5
times = [0]
times_2=[]
Positions=[]
particle=Proton()
BField=EMField(electric = np.array([0,0,0], dtype=float), magnetic = np.array([0,0,-1E-5], dtype=float))
Cyclo_Frequency=BField.Cyclotron_Frequency(particle)+32
print(Cyclo_Frequency)
square_sig=BField.Square_Wave_Gen(Cyclo_Frequency)
PB=ChargedParticleBunch()
CM=ChargedParticleBunch(electric = np.array([0,0,0], dtype=float), magnetic = np.array([0,0,-1E-5], dtype=float))
radius_of_orbit=2.9868732070658437
L=0.08
offset=1.1
Bunch_Num=150
Bunch=PB.Generate_Bunch(Bunch_Num)
Time_period=CM.Orbit_Period(Bunch)
Sine_Wave=BField.Sine_Modulator(Bunch_Num)

Average_Positons=[]
Average_Velocities=[]
Average_Kinetic_Energies=[]
i=0
it=0
iter=0
len_check=[]
while time<=5*Time_period:
    if i==0:
        T_i=PB.EnergySpread(Bunch)
        Initial_Positions,X_spread,Y_spread=PB.PositionSpread(Bunch)
        pd.DataFrame(T_i).to_csv(r'C:\Users\benti\Documents\PHYS 389\100ProtonSpreadI2.csv')
        pd.DataFrame(Initial_Positions).to_csv(r'C:\Users\benti\Documents\PHYS 389\100ProtonPosSpreadI2.csv')
       
        print('Initial Spread Saved')
        times.append(time)
        Averages=CM.Averages(Bunch)
        Average_Positons.append(Averages[0])
        Average_Velocities.append(Averages[1])
        Average_Kinetic_Energies.append(Averages[2])
        Bunch=CM.Bunch_Update(Bunch,deltat,2)
        time += deltat
        times.append(time)
        i+=1
    else:
        Y_avg=Average_Positons[-1]
        y=Y_avg[1]
        check=np.abs(y-offset)
        check2=PB.Boundary_Check(Bunch,L,offset)
        if check2==0 or check2==1:
            particles_to_acc,particle_to_constant=PB.Particle_To_Acc(Bunch,L,offset)
            particles_to_acc,particle_to_constant=np.array(particles_to_acc),np.array(particle_to_constant)
            len_check.append(len(particles_to_acc))
            len_check.append(len(particles_to_acc))
            while len(particles_to_acc)!=0:
                if len(particles_to_acc)<=(Bunch_Num-1):
                        print('enter 1')
                        it+=1
                        checker=abs(len_check[-1]-len_check[-2])
                        if checker!=0:
                            iter+=checker
                            SQ_Val=Sine_Wave[iter]*square_sig[int(SQ_Val_Multiplier*it)]
                            print(SQ_Val,len(particles_to_acc),len(particle_to_constant),checker,iter)
                            EMC=ChargedParticleBunch(electric = np.array([0,SQ_Val*0.035,0], dtype=float), magnetic = np.array([0,0,-1E-5], dtype=float))
                            Averages=EMC.Averages(Bunch)
                            Average_Positons.append(Averages[0])
                            Average_Velocities.append(Averages[1])
                            Average_Kinetic_Energies.append(Averages[2])
                            for i in range(len(Bunch)):
                                e=np.where(particles_to_acc==i)
                                c=np.where(particle_to_constant==i)
                                c=c[0]
                                e=e[0]
                                if len(c)==1:
                                    Bunch[i]=CM.Particle_Update(Bunch[i],deltat,2)
                                elif len(e)==1:
                                    Bunch[i]=EMC.Particle_Update(Bunch[i],deltat,2)
                                else:
                                    print('fail')
                            time += deltat
                            times.append(time)
                            particles_to_acc,particle_to_constant=PB.Particle_To_Acc(Bunch,L,offset)
                            particles_to_acc,particle_to_constant=np.array(particles_to_acc),np.array(particle_to_constant)
                            len_check.append(len(particles_to_acc))
                            checker=abs(len_check[-1]-len_check[-2])
                        else:
                            SQ_Val=Sine_Wave[iter]*square_sig[int(SQ_Val_Multiplier*it)]
                            print(SQ_Val,len(particles_to_acc),len(particle_to_constant),checker,iter)
                            EMC=ChargedParticleBunch(electric = np.array([0,SQ_Val*0.035,0], dtype=float), magnetic = np.array([0,0,-1E-5], dtype=float))
                            Averages=EMC.Averages(Bunch)
                            Average_Positons.append(Averages[0])
                            Average_Velocities.append(Averages[1])
                            Average_Kinetic_Energies.append(Averages[2])
                            for i in range(len(Bunch)):
                                e=np.where(particles_to_acc==i)
                                c=np.where(particle_to_constant==i)
                                c=c[0]
                                e=e[0]
                                if len(c)==1:
                                    Bunch[i]=CM.Particle_Update(Bunch[i],deltat,2)
                                elif len(e)==1:
                                    Bunch[i]=EMC.Particle_Update(Bunch[i],deltat,2)
                                else:
                                    print('fail')
                                    break
                            time += deltat
                            times.append(time)
                            particles_to_acc,particle_to_constant=PB.Particle_To_Acc(Bunch,L,offset)
                            particles_to_acc,particle_to_constant=np.array(particles_to_acc),np.array(particle_to_constant)
                            len_check.append(len(particles_to_acc))
                            checker=abs(len_check[-1]-len_check[-2])
                elif len(particles_to_acc)==Bunch_Num:
                    iter=Bunch_Num-2
    
                    it+=1
                    SQ_Val=square_sig[int(SQ_Val_Multiplier*it)]
                    EMC=ChargedParticleBunch(electric = np.array([0,SQ_Val*0.035,0], dtype=float), magnetic = np.array([0,0,-1E-5], dtype=float))
                    Averages=EMC.Averages(Bunch)
                    Average_Positons.append(Averages[0])
                    Average_Velocities.append(Averages[1])
                    Average_Kinetic_Energies.append(Averages[2])
                    for i in range(len(Bunch)):
                        e=np.where(particles_to_acc==i)
                        c=np.where(particle_to_constant==i)
                        c=c[0]
                        e=e[0]
                        if len(c)==1:
                            Bunch[i]=CM.Particle_Update(Bunch[i],deltat,2)
                        elif len(e)==1:
                            Bunch[i]=EMC.Particle_Update(Bunch[i],deltat,2)
                        else:
                            print('fail')
                    time += deltat
                    times.append(time)
                    particles_to_acc,particle_to_constant=PB.Particle_To_Acc(Bunch,L,offset)
                    particles_to_acc,particle_to_constant=np.array(particles_to_acc),np.array(particle_to_constant)

        else:
            iter=0
            Averages=CM.Averages(Bunch)
            Average_Positons.append(Averages[0])
            Average_Velocities.append(Averages[1])
            Average_Kinetic_Energies.append(Averages[2])
            Bunch=CM.Bunch_Update(Bunch,deltat,2)
            time+=deltat
            times.append(time)
            it+=1
T_f=PB.EnergySpread(Bunch)
positionF,X_spread,Y_spread=PB.PositionSpread(Bunch)

pd.DataFrame(T_f).to_csv(r'C:\Users\benti\Documents\PHYS 389\100ProtonSpreadF2.csv')
pd.DataFrame(positionF).to_csv(r'C:\Users\benti\Documents\PHYS 389\100ProtonPosSpreadF2.csv')


pd.DataFrame(Average_Positons).to_csv(r'C:\Users\benti\Documents\PHYS 389\100ProtonPositions2.csv')
pd.DataFrame(Average_Kinetic_Energies).to_csv(r'C:\Users\benti\Documents\PHYS 389\100ProtonKineticEnergy2.csv')
pd.DataFrame(times).to_csv(r'C:\Users\benti\Documents\PHYS 389\100ProtonTimes2.csv')
print('All information has been saved')