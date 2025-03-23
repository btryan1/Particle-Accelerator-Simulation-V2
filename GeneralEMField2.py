from abc import ABC, abstractmethod
from cmath import pi
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import signal
class GeneralEMField(ABC):#our GeneralEMField class which inheriance abstract methods. 

    @abstractmethod#initilaises our class
    def __init__(self, ElectricField = np.array([0,0,0], dtype=float), MagneticField = np.array([0,0,0], dtype=float)):
        self.electric = np.array(ElectricField,dtype=float)
        self.magnetic = np.array(MagneticField, dtype=float)
        super(GeneralEMField, self).__init__()


    def __repr__(self):#defines the string representation returned when the class initlized is called
        return 'EMField: E = {0}, B = {1}'.format(self.electric,self.magnetic)

    #caluclate the acceleration using the lorentz force for charged particles
    def getAcceleration(self,particle):
        lorentz = np.array(self.electric, dtype=float)
        lorentz+=np.cross(particle.velocity, self.magnetic)
        lorentz *= (particle.charge/particle.mass)
        return lorentz
    
class EMField(GeneralEMField):#a subclass using the super class above and inheritance, this is the class method we call due to the dynamic methods inside which are less abstract
        
    def __init__(self,electric = np.array([0,0,0], dtype=float),magnetic = np.array([0,0,0], dtype=float)):
        super().__init__(electric,magnetic)#definies our inital class values
  
    def TimePeriod(self,particle):#class method to calculate the time period of the cyclotron
        return (2*pi*particle.mass)/(particle.charge*np.linalg.norm(self.magnetic))

    def Cyclotron_Frequency(self,particle):#class method to calculate the cyclotron frequency
        return (particle.charge*np.linalg.norm(self.magnetic))/(particle.mass)
    
    def Cyclotron_Radius(self,particle):#class method to calculate the cycltron radius
        return (particle.mass)*(np.linalg.norm(particle.velocity))/((particle.charge*np.linalg.norm(self.magnetic)))

    def Square_Wave_Gen(self,f_cyclo):#class method that returns our modulate square wave which is used as one of the RF sources in our cyclotron
        t = np.linspace(0, 0.2, 200000, endpoint=False)
        square=signal.square(f_cyclo * t)
        I=[]
        for i in range(664):
            I.append(1)
        for j in range(len(square)):
            I.append(square[j])
        return I

    def Linear_Square_Wave_Gen(self,f):#The square wave used as the RF source in our LINAC simulation
        t = np.linspace(0, 0.2, 200000, endpoint=False)
        square=signal.square(f * t) 
        return square,t

    def Sine_Modulator(self,rate):#This class method is what modulates our square wave in the other RF source for our second cycltron simulation.
        sample_rate = rate
        start_time = 0
        end_time = 1
        time = np.arange(start_time, end_time, 1/sample_rate)
        frequency = 0.25
        amplitude = 0.1
        theta = 0
        sinewave = amplitude * np.sin(2 * np.pi * frequency * time + theta)
        sinewave2=sinewave[::-1]
        sineWave=0.9+np.concatenate((sinewave,sinewave2))
        return sineWave
