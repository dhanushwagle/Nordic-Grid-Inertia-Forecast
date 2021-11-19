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
y = 0
num = len(SGT)
for i in range(num):
    H = SGT[i].h #Here, h is an attribute of Inertia in Simulation RMS of SG Type
    app.PrintPlain('Moment of Inertia of the Generator: %s = %.6f sec' %(i+1,H))
    S = SG[i].sgini_a
    app.PrintPlain('Rated Power of the Generator:       %s = %.6f MVA \n' %(i+1,S))
    S_sys += S
    y += (S*H)
    
H_sys = y/S_sys
KE_system = S_sys*H_sys
app.PrintPlain('Rated Power of the System:                 = %.6f GW' %(S_sys/1000))
app.PrintPlain('Inertia of the System:                     = %.6f sec' %(H_sys))
app.PrintPlain('Kinetic Energy of the System:              = %.6f GWs\n' %(KE_system/1000))
