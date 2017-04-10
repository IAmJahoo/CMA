#!/usr/bin/python
#Jan Horbowicz

import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt
import phase_functions as pf

NumberList=[5,16,19,20,21,22,24,29,44,47,50,55,59,75,76,77,79,91,102,\
    105,110,119,124,126,130,190,201,214,303,313,354,419,423,433,444,\
    615,620,954,2867]
VMagCorr,Phase=[],[]

print "dostepne numery planetoidy: "
print NumberList
AsterNumb=raw_input("Podaj numer planetoidy: ")

data=open("alldata.dat","r")
line=data.readline().split()
while line[0] != AsterNumb:
	#waiting for right number
    line=data.readline().split()
Phase.append(float(line[8]))
VMagCorr.append(float(line[11]))

while line[0] == AsterNumb:
    Phase.append(float(line[8]))
    VMagCorr.append(float(line[11]))
    line=data.readline().split()
data.close()
Phase = np.array(Phase)
VMagCorr = np.array(VMagCorr)
popt, pcov = curve_fit(pf.PhaseFunc, Phase, VMagCorr)
plt.plot(Phase, VMagCorr, 'o')
plt.plot(Phase, pf.PhaseFunc(Phase, popt[0], popt[1]), 'r-')
plt.title(AsterNumb)
plt.xlabel('Phase Angle')
plt.ylabel('Johnsons V Magnitude')
plt.gca().invert_yaxis()
plt.show()
