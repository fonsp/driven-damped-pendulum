import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

'''
De vergelijking is:

Ф'' + 2 β Ф' + ω0 ^2 sin(Ф) - γ ω0 ^2 cos(ωt)
 -- (12.11) in Taylor

Scipy wil alleen 1ste-orde ODEs oplossen, daarom de substitutie:

x2 = Ф'
x1 = Ф

Dan krijgen we

x1' = x2
x2' = -[2 β x2 + ω0 ^2 sin(x1) - γ ω0 ^2 cos(ωt)]

'''

# Parameters voor de ODE:
ω = 2*np.pi             # p.464
ω0pow2 = (1.5*ω)**2     # p.464
β = 1.5*ω/4             # p.464, voetnoot 6
γ = .42                 # variabel
Ф0 = 0                  # p.464, voetnoot 6
sampleFreq = 10000      # geen idee, aantal 'frames per seconde' van de simulatie

def fun(Y, t):
    return [Y[1], -(2*β*Y[1] + ω0pow2 * np.sin(Y[0]) - γ * ω0pow2 * np.cos(ω*t))]

# Hier komen de punten in voor de scatter plot, in de vorm [[x,y],[x,y],...]
# dus in dit geval [[1.06,Ф(500)],[1.06,Ф(501)],...,[1.06,Ф(599)],[1.0605,Ф(500)],...]
graphPoints = []


# Spreiding van punten op de x-as, Taylor gebruikt 0.0001
γSampleDistance = .0005

for γ in np.arange(1.06, 1.087, γSampleDistance):
    # Voor elke waarde voor gamma integreren we de ODE in het volgende tijdsgebied:
    a_t = np.arange(0, 600.0, 1/sampleFreq)

    # Ik bedenk me nu dat odeint eigenlijk γ als parameter moet hebben maar python
    # heeft geen scope dus alles is oke
    asol = integrate.odeint(fun, [Ф0, 0], a_t)
    # De eerste kolom (x1) is dus de uitweiking, met plt.plot(a_t,y) zie je een grafiek
    # van uitweiking vs tijd
    y = asol[:,0]
    # sampler bevat de indices van t=500, t=501, ..., t=599
    sampler = [sampleFreq*x for x in range(500,600)]
    # ySamples bevat Ф(500), Ф(501), ..., Ф(599)
    ySamples = asol[sampler,0]

    # Voeg de 100 nieuwe punten toe aan de dataset
    newGraphPoints = [[γ, yVal % 2*np.pi] for yVal in ySamples]
    graphPoints = graphPoints + newGraphPoints

# Plot de dataset
graphMatrx = np.array(graphPoints)
plt.scatter(graphMatrx[:,0], graphMatrx[:,1])
#plt.plot(a_t, y)
plt.show()