import powerfactory #importing powerfactory module
app = powerfactory.GetApplication() # defining application object
app.ClearOutputWindow() # Clearing Output Window

#Get grid as a target folder
TargetGrid = app.GetCalcRelevantObjects("Grid.ElmNet")

#Getting Synchronous Generator
SG = app.GetCalcRelevantObjects('*.ElmSym')[0:]

#Getting Synchronous Generator Type
SGT = app.GetCalcRelevantObjects('*.TypSym')[0:]
S_sys = 0
H_sys = 0
pf =  0
y = 0
num = len(SGT)
for i in range(num):
    H = SGT[i].h #Here, h is an attribute of Inertia in Simulation RMS of SG Type
    app.PrintPlain('Moment of Inertia of the Generator:    %s = %.1f sec' %(i+1,H))
    #S1 = SG[i].sgini_a
    #app.PrintPlain('SG Rated Power of the Generator:       %s = %.6f MVA' %(i+1,S1))
    S = SGT[i].sgn
    app.PrintPlain('SGT Rated Power of the Generator:      %s = %.1f MVA' %(i+1,S))
    pf = SGT[i].cosn #Here, h is an attribute of Inertia in Simulation RMS of SG Type
    app.PrintPlain('Power Factor of the Generator:         %s = %.2f' %(i+1,pf))
    S_sys += (S*pf)
    app.PrintPlain('Active Power of the Generator:         %s = %.6f MW\n' %(i+1,S*pf))
    y += (S*H)

H_sys = y/S_sys

#System Parameters
app.PrintPlain('System Parameters:')
app.PrintPlain('---------------------------------------------------------------')
KE_system = S_sys*H_sys
app.PrintPlain('Rated Power of the System:                 = %.6f MW' %(S_sys))
app.PrintPlain('Inertia of the System:                     = %.6f sec' %(H_sys))
app.PrintPlain('Kinetic Energy of the System:              = %.6f MWs' %(KE_system))
app.PrintPlain('---------------------------------------------------------------')

#List of inertia points from INPS (30 samples, single sample per minute) forcasted using 1 mnth data
inertia = [2.074796, 2.074378, 2.073964, 2.073554, 2.073149, 2.072748,
             2.072351, 2.071959, 2.071571, 2.071187, 2.070808, 2.070433,
             2.070062, 2.069696, 2.069334, 2.068977, 2.068624, 2.068276,
             2.067932, 2.067592, 2.067257, 2.066927, 2.066601, 2.066280,
             2.065964, 2.065652, 2.065344, 2.065041, 2.064743, 2.064450]
             
#Calculation from the Datas of Nordic Grid
app.PrintPlain('Kinectic Energy (MWs) using Forcasted Data:')
app.PrintPlain('---------------------------------------------------------------') 
count = 1
for values in inertia:
    KE = values*S_sys
    app.PrintPlain('%d:   =    %.6f' %(count,KE))
    count += 1

app.PrintPlain('---------------------------------------------------------------')    
