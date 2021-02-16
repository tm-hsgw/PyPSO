import sys
import numpy as np
import Target as tgt


class Particle :
    def __init__(self, x) :
        import ParticleSwarmOptimization as pso
        self.__x = np.array(x)
        self.__pb = np.array(x)
        self.__err = tgt.Evaluate(pso.target, self.__x)
        self.__pbErr = self.__err
        self.Velocity = np.zeros(len(x))

    @property
    def Position(self) :
        return self.__x
    
    @property
    def Error(self) :
        return self.__err

    @property
    def PersonalBest(self) :
        return self.__pb

    @property
    def PersonalBestError(self) :
        return self.__pbErr

    def Move(self) :
        import ParticleSwarmOptimization as pso
        # for d in range(len(self.__x)):
        #     self.__x[d] += self.Velocity[d]
        self.__x += self.Velocity

        self.__err = tgt.Evaluate(pso.target, self.__x)

        if self.__err < self.__pbErr :
            self.__pbErr = self.__err
            self.__pb = self.__x.copy()