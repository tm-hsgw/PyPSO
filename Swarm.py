import sys
import numpy as np
import random
import Particle as ptc

class Swarm :
    __w = 0.7
    __cp = 1.4
    __cg = 1.4

    def __init__(self, min, max, number) :
        self.__dim = len(max)
        self.__gb = np.zeros(len(max))
        self.__gbErr = sys.float_info.max
        self.Swarm = []
        for p in range(number):
            x = [random.uniform(min[d], max[d]) for d in range(self.__dim)]
            self.Swarm.append(ptc.Particle(x))
            # initialize velocities randomly
            # self.Member[p].V = [random.uniform(min[i], max[i]) for i in range(self.Dim)]
            
            if(self.Swarm[p].PersonalBestError < self.__gbErr):
                self.__gbErr = self.Swarm[p].PersonalBestError
                self.__gb = self.Swarm[p].PersonalBest.copy()

    @property
    def GlobalBest(self) :
        return self.__gb

    @property
    def GlobalBestError(self) :
        return self.__gbErr

    def Move(self, epoch) :
        newError = sys.float_info.max
        newPosition = []
        update = False
        for particle in self.Swarm:
            rp = self.__cp * random.random()
            rg = self.__cg * random.random()

            for d in range(self.__dim):
                x = particle.Position[d]
                v = self.__w * particle.Velocity[d]
                v += rp * (particle.PersonalBest[d] - x)
                v += rg * (self.__gb[d] - x)
                particle.Velocity[d] = v

            particle.Move()

            if particle.PersonalBestError < self.__gbErr:
                newError = particle.PersonalBestError
                newPosition = particle.PersonalBest.copy()
                update = True

        if update:
            self.__gbErr = newError
            self.__gb = newPosition.copy()
            # print(epoch, '{:.5e}'.format(self.__gbErr))