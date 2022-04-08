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
    
    nsec = np.loadtxt(f'../build/{projectile}_{energy}_{target}_{nevents}.csv', usecols=(5))

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
projectile = 'pion'
target='Fe'
nevents='1M'
phys_model='FTFP_BERT_ATL'
nsec_01 = np.loadtxt(f'../build/{projectile}_01GeV_{target}_{nevents}.csv', usecols=(5))
nsec_05 = np.loadtxt(f'../build/{projectile}_05GeV_{target}_{nevents}.csv', usecols=(5))
nsec_10 = np.loadtxt(f'../build/{projectile}_10GeV_{target}_{nevents}.csv', usecols=(5))
nsec_15 = np.loadtxt(f'../build/{projectile}_15GeV_{target}_{nevents}.csv', usecols=(5))
nsec_20 = np.loadtxt(f'../build/{projectile}_20GeV_{target}_{nevents}.csv', usecols=(5))
nsec_25 = np.loadtxt(f'../build/{projectile}_25GeV_{target}_{nevents}.csv', usecols=(5))
nsec_30 = np.loadtxt(f'../build/{projectile}_30GeV_{target}_{nevents}.csv', usecols=(5))

plt.figure(figsize=(10,8))

plt.hist(nsec_01, bins=np.arange(0,76,1), density=True, histtype='step', label=f'Energy: 100 MeV')
plt.hist(nsec_05, bins=np.arange(0,76,1), density=True, histtype='step', label=f'Energy: 500 MeV')
plt.hist(nsec_10, bins=np.arange(0,76,1), density=True, histtype='step', label=f'Energy: 10 GeV')
plt.hist(nsec_15, bins=np.arange(0,76,1), density=True, histtype='step', label=f'Energy: 15 GeV')
plt.hist(nsec_20, bins=np.arange(0,76,1), density=True, histtype='step', label=f'Energy: 20 GeV')
plt.hist(nsec_25, bins=np.arange(0,76,1), density=True, histtype='step', label=f'Energy: 25 GeV')
plt.hist(nsec_30, bins=np.arange(0,76,1), density=True, histtype='step', label=f'Energy: 30 GeV')

plt.xlabel('Number of secondary particles')
plt.ylabel('Fraction of events')
plt.title(fr'{nevents} events; {projectile} $\rightarrow$ {target} target')
plt.legend()
plt.savefig(f'plots/nsec_{projectile}_various_energy_{target}_{nevents}_2.png')
