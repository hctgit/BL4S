import root_numpy
import matplotlib.pyplot as plt
from ROOT import TFile
import numpy as np

samplerdict = {
    'mark1_"all"'                : "Total",
    'mark1_"electrons"'          : "e$^{-}$",
    'mark1_"positrons"'          : "e$^{+}$",
    #'mark1_"gamma"'              : "$\gamma$",
    'mark1_"primaryProtons"'     : "p (primary)",
    'mark1_"secondaryProtonsPM"' : "p (secondary)",
    'mark1_"neutrons"'           : "n",
    #'mark1_"muonsPM"'            : "$\mu^{\pm}$",
    'mark1_"pions0PM"'           : "$\pi^{\pm,\mathrm{O}}$",
    'mark1_"kaons"'              : "K$^{\mathrm{0}(S,L),\pm}$",
    'mark1_"lambda"'             : "$\Lambda$",
    'mark1_"sigma"'              : "$\Sigma^{\pm,\mathrm{O}}$",
    'mark1_"xi"'                 : "$\Xi^{O,-,*O}$",
    'mark1_"omega"'              : "$\Omega^{\pm}$"
    }

def Plot(filename, title=None):
    f = TFile(filename)

    entries = f.Get("PhitsHisto").GetEntries()
    fig = plt.figure(figsize=(12,6))
    for key,label in samplerdict.iteritems():
        x,y = ConvertTH1(f.Get(key))
        plt.hist(x,len(y),weights=y/entries,label=label,histtype="step")

    fig.get_axes()[0].set_yscale('log')
    plt.xlabel('Energy (GeV)')
    plt.ylabel('Particle / Primary / 12 MeV (GeV$^{-1}$)')
    plt.xlim(-0.5,26.5)
    plt.legend(fontsize='small')
    plt.subplots_adjust(left=0.1,right=0.97)
    if (title!=None):
        plt.title(title)
    
    plt.draw()


def ConvertTH1(rootHisto):
    binCentres = np.array([rootHisto.GetBinCenter(i) for i in range(len(rootHisto))])
    binValues  = np.array(rootHisto)
    return binCentres, binValues
                          
