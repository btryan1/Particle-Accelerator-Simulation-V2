
#installs all the need modules and classes
from Particle import Proton,AntiProton,DeuteriumNucleus,AntiDeuteriumNucleus
from GeneralEMField2 import EMField
import numpy as np

ParticleType=Proton

class ChargedParticleBunch(ParticleType):
    def __init__(self,electric = np.array([0,0,0], dtype=float), magnetic = np.array([0,0,0], dtype=float)):
        self.electric=electric
        self.magnetic=magnetic

    def Generate_Bunch(self,particle_num):#this generates our random particle bunch, which has a gaussian distrubution for its velocities and positions. The particle type and distributions is all controllable
        Bunch=[]                      
        mean = [0.0002, 0.0002, 0]
        mean_2_cyclo=[900,1200,0]
        mean_2_linear=[1000,0,0]
        position_matrix = [[0.0001, 0, 0], [0, 0.0001, 0], [0, 0, 0.0001]]
        velocity_matrix_cyclo=[[1000, 0, 0], [0, 1115, 0], [0, 0, 0]]
        velocity_matrix_linear=[[1000, 0, 0], [0, 0, 0], [0, 0, 0]]
        # using np.multinomial() method
        particle_positions = np.random.multivariate_normal(mean, position_matrix, particle_num)
        particle_velocities=np.random.multivariate_normal(mean_2_linear, velocity_matrix_linear, particle_num)
        for i in range(particle_num):#initilises each particle as its own class instance thus return an array of indivual particles which can each be indivually manipulated i.e. they are distiguishable in this simulation sense
            particle=ParticleType()
            particle.position=particle_positions[i]
            particle.velocity=particle_velocities[i]
            Bunch.append(particle)
        return Bunch
    
    def Bunch_Update(self,bunch,deltaT,method):#our class method that updates the particles within the bunch
        BField= EMField(self.electric,self.magnetic)
        for i in range(len(bunch)):
            particle=bunch[i]
            acceleration=BField.getAcceleration(particle)
            particle.update(deltaT,method,acceleration)
            bunch[i]=particle
        return bunch
    def Particle_Update(self,particle,deltaT,method):#updates specific particles
        BField= EMField(self.electric,self.magnetic)
        acceleration=BField.getAcceleration(particle)
        particle.update(deltaT,method,acceleration)
        return particle
    def Orbit_Period(self,bunch):#a class method that calculates the max orbit period of our protons
        BField= EMField(self.electric,self.magnetic)
        Orbit_Period=[]
        for i in range(len(bunch)):
            Orbit_Period.append(BField.TimePeriod(bunch[i]))
        return (max(Orbit_Period))
        
    
    def Averages(self,bunch):
        Type=ParticleType()
        positions=[]
        velocities=[]
        for i in range(len(bunch)):
            Particle=bunch[i]
            positions.append(Particle.position)
            velocities.append(Particle.velocity)
        positions=np.vstack(positions)
        velocities=np.stack(velocities)
        average_position=np.array([np.mean(positions[:,0]),np.mean(positions[:,1]),np.mean(positions[:,2])],dtype=float)
        average_velocity=np.array([np.mean(velocities[:,0]),np.mean(velocities[:,1]),np.mean(velocities[:,2])],dtype=float)
        average_kinetic_energy=0.5*Type.mass*(np.linalg.norm(average_velocity))**2
        return [average_position,average_velocity,average_kinetic_energy]
    
    def Boundary_Check(self,bunch,L,offset):
        positions=[]
        for i in range(len(bunch)):
            Particle=bunch[i]
            positions.append(Particle.position[1])

        Min=min(positions)
        Max=max(positions)
        check1=np.abs(Min-offset)
        check2=np.abs(Max-offset)
        if check1<=L:
            print(Min,Max)
            return 0
        elif check2<=L:
            print(Min,Max)
            return 1
        else:
            return 2

    def Particle_To_Acc(self,bunch,L,offset):
        particles_to_acc=[]
        particle_to_constant=[]
        for i in range(len(bunch)):
            Particle=bunch[i]
            position=Particle.position
            poscheck=np.abs(position[1]-offset)
            if poscheck<=L:
                particles_to_acc.append(i)
            else:
                particle_to_constant.append(i)
        return particles_to_acc,particle_to_constant

    def PositionSpread(self,bunch):
        positions=[]
        for i in range(len(bunch)):
            Particle=bunch[i]
            positions.append(Particle.position)
        MinX=min(positions[0])
        MaxX=max(positions[0])
        MinY=min(positions[1])
        MaxY=max(positions[1])
        X_spread=MaxX-MinX
        Y_spread=MaxY-MinY
        return positions,MinY,MaxY

    def EnergySpread(self,bunch):
        T=[]
        for i in range(len(bunch)):
            Particle=bunch[i]
            T.append(0.5*Particle.mass*(np.linalg.norm(Particle.velocity))**2)
        return T

