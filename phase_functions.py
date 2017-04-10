#!/usr/bin/python
#Jan Horbowicz
import numpy as np
#H - absolute magnitude of an asteroid
#G - slope parameter
def PhaseFunc(PhaseAngle,H,G):
    PhaseAngle = PhaseAngle*np.pi/180.0
    w=np.exp(-90.56*np.tan(0.5*PhaseAngle)**2)
    PHI1 = (w*(1 - 0.986*np.sin(PhaseAngle)/(0.119 + 1.341*\
        np.sin(PhaseAngle) - 0.754*np.sin(PhaseAngle)**2)) + \
        (1-w)*np.exp(-3.332*np.tan(0.5*PhaseAngle)**0.631))
    PHI2 = (w*(1 - 0.238*np.sin(PhaseAngle)/(0.119 + 1.341*\
        np.sin(PhaseAngle) - 0.754*np.sin(PhaseAngle)**2)) + \
        (1-w)*np.exp(-1.862*np.tan(0.5*PhaseAngle)**1.218))
    return H - 2.5*np.log10((1-G)*PHI1+G*PHI2)

