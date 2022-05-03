import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
matplotlib.style.use('paper.mplstyle')

"""
This file make distribution plots of 
kinematic variables produced by G4.
"""


def plot_nsec_distribution(projectile, energy, target, nevents, randE, randDir, phys_model, bins):
    """
    Plot the distribution of number of secondary particles given params in csv file name. 
    """
    
    nsec = np.loadtxt(f'../build/{projectile}_{energy}_{target}_{nevents}.csv', usecols=(6))

    plt.figure(figsize=(10,8))
    plt.hist(nsec, bins=bins, density=True, ec='black', label=f'model: {phys_model}')
    plt.xlabel('Number of secondary particles')
    plt.ylabel('Fraction of events')
    plt.title(fr'{nevents} events; {projectile} ({energy}) $\rightarrow$ {target} target')
    plt.legend()
    plt.savefig(f'plots/nsec_{projectile}_{energy}_{target}_{nevents}.png')


""" sanity-check plot """
# plot_nsec_distribution(projectile='pion', 
#                        energy='25GeV',
#                        target='H',
#                        nevents='100K',
#                        randE=False,
#                        randDir=False,
#                        phys_model='FTFP_BERT_ATL',
#                        bins=np.linspace(0,20,20))

# """ pion - Fe plot """
# plot_nsec_distribution(projectile='pion', 
#                        energy='20GeV',
#                        target='Fe',
#                        nevents='100K',
#                        randE=False,
#                        randDir=False,
#                        phys_model='FTFP_BERT_ATL',
#                        bins=np.linspace(0,75,20))

# plot_nsec_distribution(projectile='pion', 
#                        energy='25GeV',
#                        target='Fe',
#                        nevents='100K',
#                        randE=False,
#                        randDir=False,
#                        phys_model='FTFP_BERT_ATL',
#                        bins=np.linspace(0,75,20))

# plot_nsec_distribution(projectile='pion', 
#                        energy='30GeV',
#                        target='Fe',
#                        nevents='100K',
#                        randE=False,
#                        randDir=False,
#                        phys_model='FTFP_BERT_ATL',
#                        bins=np.linspace(0,75,20))


""" combined plot of all generation energies """

def plot_all_events(t='Fe', n='100K'):
    projectile = 'pion'
    target=t
    nevents=n
    phys_model='FTFP_BERT_ATL'

    nsec_01 = np.loadtxt(f'../build/{projectile}_01GeV_{target}_{nevents}.csv', usecols=(6))
    nsec_05 = np.loadtxt(f'../build/{projectile}_05GeV_{target}_{nevents}.csv', usecols=(6))
    nsec_1  = np.loadtxt(f'../build/{projectile}_1GeV_{target}_{nevents}.csv', usecols=(6))
    nsec_5  = np.loadtxt(f'../build/{projectile}_5GeV_{target}_{nevents}.csv', usecols=(6))
    nsec_10 = np.loadtxt(f'../build/{projectile}_10GeV_{target}_{nevents}.csv', usecols=(6))
    nsec_11 = np.loadtxt(f'../build/{projectile}_11GeV_{target}_{nevents}.csv', usecols=(6))
    nsec_12 = np.loadtxt(f'../build/{projectile}_12GeV_{target}_{nevents}.csv', usecols=(6))
    nsec_15 = np.loadtxt(f'../build/{projectile}_15GeV_{target}_{nevents}.csv', usecols=(6))
    nsec_20 = np.loadtxt(f'../build/{projectile}_20GeV_{target}_{nevents}.csv', usecols=(6))
    nsec_25 = np.loadtxt(f'../build/{projectile}_25GeV_{target}_{nevents}.csv', usecols=(6))
    nsec_30 = np.loadtxt(f'../build/{projectile}_30GeV_{target}_{nevents}.csv', usecols=(6))

    nsces = [nsec_01, nsec_05, nsec_1, nsec_5, nsec_10, nsec_11, nsec_12, nsec_15, nsec_20, nsec_25, nsec_30]
    energies = ['100 MeV', '500 MeV', '1 GeV', '5 GeV', '10 GeV', '11 GeV', '12 GeV', '15 GeV', '20 GeV', '25 GeV', '30 GeV']
    
    plt.figure(figsize=(10,8))

    cmap = matplotlib.cm.get_cmap('Spectral_r')

    for i in range(len(nsces)):
        plt.hist(nsces[i], bins=np.arange(0,76,1), density=True, histtype='step', label=f'Energy: {energies[i]}', color=cmap(i/len(nsces)))
        print(f'N events at {energies[i]}: {len(nsces[i])}')

    plt.xlabel('Number of secondary particles')
    plt.ylabel('Fraction of events')
    plt.title(fr'{nevents} events; {projectile} $\rightarrow$ {target} target')
    plt.legend()
    plt.savefig(f'plots/nsec_{projectile}_various_energy_{target}_{nevents}.png')

plot_all_events('Fe', '1M')
plot_all_events('Cu', '1M')


""" compare Fe/Cu at various energies """

def compare_Fe_Cu(n='1M'):
    projectile = 'pion'

    nevents=n
    phys_model='FTFP_BERT_ATL'


    etag = ['01', '05', '1', '5', '10', '11', '12', '15', '20', '25', '30']
    energies = ['100 MeV', '500 MeV', '1 GeV', '5 GeV', '10 GeV', '11 GeV', '12 GeV', '15 GeV', '20 GeV', '25 GeV', '30 GeV']
    
    for i in range(len(etag)):

        nsec_Fe = np.loadtxt(f'../build/{projectile}_{etag[i]}GeV_Fe_{nevents}.csv', usecols=(6))
        nsec_Cu = np.loadtxt(f'../build/{projectile}_{etag[i]}GeV_Cu_{nevents}.csv', usecols=(6))

        plt.figure(figsize=(10,8))

        plt.hist(nsec_Fe, bins=np.arange(0,76,1), density=True, histtype='step', label=f'Fe', color='brown')
        plt.hist(nsec_Cu, bins=np.arange(0,76,1), density=True, histtype='step', label=f'Cu', color='darkcyan')

        plt.xlabel('Number of secondary particles')
        plt.ylabel('Fraction of events')
        plt.title(f'Comparing Fe/Cu at {energies[i]}, {nevents} events')
        plt.legend()
        plt.savefig(f'plots/nsec_FeCu_compariso_{etag[i]}GeV_{nevents}.png')

compare_Fe_Cu('1M')